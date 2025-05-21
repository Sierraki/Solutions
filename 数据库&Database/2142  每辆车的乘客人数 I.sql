WITH a1 AS
(
	SELECT  bus_id
	       ,ifnull((1+lag(arrival_time) OVER (order by arrival_time)),1) start
	       ,arrival_time end
	FROM buses
), a2 AS
(
	SELECT  bus_id
	       ,COUNT(*) cnt
	FROM passengers p
	CROSS JOIN a1
	WHERE arrival_time BETWEEN start AND end
	GROUP BY  bus_id
)
SELECT  b.bus_id
       ,ifnull(cnt,0) passengers_cnt
FROM buses b
LEFT JOIN a2
ON b.bus_id = a2.bus_id
ORDER BY b.bus_id