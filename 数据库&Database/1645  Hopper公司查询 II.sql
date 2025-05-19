WITH recursive full_month AS
(
	SELECT  1 AS month
	UNION
	SELECT  month+1 AS month
	FROM full_month
	WHERE month <= 11 
), month_drivers AS
(
	SELECT  COUNT(driver_id) AS nums
	       ,if(year(join_date) < '2020',1,month(join_date)) month
	FROM Drivers
	WHERE year(join_date) <= '2020'
	GROUP BY  month
), month_active AS
(
	SELECT  month(requested_at) month
	       ,COUNT(distinct driver_id) AS counts
	FROM Rides r
	LEFT JOIN AcceptedRides a
	ON r.ride_id = a.ride_id
	WHERE year(requested_at) = '2020'
	GROUP BY  month
)
SELECT  month
       ,if(driver_num = 0,0,round(actice_num/driver_num*100,2)) AS working_percentage
FROM
(
	SELECT  t1.month
	       ,ifnull(SUM(t2.nums) over(order by month),0) AS driver_num
	       ,ifnull(t3.counts,0)                         AS actice_num
	FROM full_month t1
	LEFT JOIN month_drivers t2
	ON t1.month = t2.month
	LEFT JOIN month_active t3
	ON t3.month = t1.month
) AS t
GROUP BY  month
ORDER BY  month