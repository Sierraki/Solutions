WITH a1 AS
(
	SELECT  bus_id
	       ,lag(arrival_time) OVER (order by arrival_time) + 1 start
	       ,arrival_time end
	       ,capacity
	FROM buses
) , a2 AS
(
	SELECT  bus_id
	       ,ifnull(start,1) start
	       ,end
	       ,capacity
	       ,arrival_time
	FROM a1
	CROSS JOIN passengers p
) , a3 AS
(
	SELECT  bus_id
	       ,start
	       ,end
	       ,COUNT(*)cnt
	FROM a2
	WHERE arrival_time BETWEEN start AND end
	GROUP BY  bus_id
) , a4 AS
(
	SELECT  bus_id
	       ,arrival_time
	       ,capacity
	       ,ifnull(cnt,0) cnt
	FROM buses
	LEFT JOIN a3 USING
	(bus_id
	)
) , a5 AS
(
	SELECT  bus_id
	       ,arrival_time
	       ,capacity
	       ,cnt
	       ,@che := if(@rest + cnt > capacity,capacity,@rest + cnt) che
	       ,@rest := if(@rest + cnt - capacity >= 0,@rest + cnt - capacity,0) r
	FROM a4,
	(
		SELECT  @che := 0
		       ,@rest := 0
	) init
)
SELECT  bus_id
       ,che passengers_cnt
FROM a5
ORDER BY bus_id