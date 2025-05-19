-- CTE生成2020年每月的最后一天
WITH RECURSIVE months AS
(
	SELECT  LAST_DAY('2019-12-01') AS month_end -- 初始日期的前一个月的最后一天 
	UNION ALL
	SELECT  LAST_DAY(month_end + INTERVAL 1 DAY) -- 下一个月的最后一天 
	FROM months
	WHERE month_end < '2020-12-01' -- 递归结束条件 
 
) , months2020 AS
(
	SELECT  *
	       ,DATE_FORMAT(month_end,'%Y-%m') AS `month` -- 格式化日期，只保留年月 
	FROM months
	WHERE DATE_FORMAT(month_end, '%Y') = "2020" 
) , t1 as(
SELECT  months2020.`month`
       ,ifnull(SUM( ar.ride_distance) ,0 ) AS ride_distance
       ,ifnull(SUM( ar.ride_duration) ,0)  AS ride_duration
FROM months2020
LEFT JOIN Rides r
ON months2020.`month` = DATE_FORMAT(r.requested_at, "%Y-%m")
LEFT JOIN AcceptedRides ar
ON ar.ride_id = r.ride_id
GROUP BY  months2020.`month` )
SELECT  *
FROM
(
	SELECT  MONTH(str_to_date(`month`,'%Y-%m'))                                                                                  AS `month`
	       ,round(AVG(ride_distance) OVER ( ORDER BY  str_to_date(`month`,'%Y-%m') ROWS BETWEEN CURRENT ROW AND 2 following ),2) AS average_ride_distance
	       ,round(AVG(ride_duration) OVER ( ORDER BY str_to_date(`month`,'%Y-%m') ROWS BETWEEN CURRENT ROW AND 2 following ),2)  AS average_ride_duration
	FROM t1
) result_to_be_truncated
WHERE `month` <= 10