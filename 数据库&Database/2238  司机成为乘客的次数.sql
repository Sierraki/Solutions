WITH a1 AS
(
	SELECT  distinct driver_id
	FROM rides
), a2 AS
(
	SELECT  a1.driver_id
	       ,COUNT(*) cnt
	FROM rides r1
	LEFT JOIN a1
	ON r1.passenger_id = a1.driver_id
	WHERE a1.driver_id is not null
	GROUP BY  a1.driver_id
)
SELECT  a1.driver_id
       ,ifnull(cnt,0) cnt
FROM a1
LEFT JOIN a2
ON a1.driver_id = a2.driver_id