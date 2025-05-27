SELECT  seat_id
FROM
(
	SELECT  seat_id
	       ,cc
	       ,COUNT(seat_id) over(PARTITION BY cc ) AS dd
	FROM
	(
		SELECT  seat_id
		       ,seat_id-AA AS cc
		FROM
		(
			SELECT  seat_id
			       ,free
			       ,rank()over(order by seat_id ASC) AS AA
			FROM cinema
			WHERE free = 1 
		)t1
	)t2
)t3
WHERE dd >= 2
ORDER BY seat_id asc