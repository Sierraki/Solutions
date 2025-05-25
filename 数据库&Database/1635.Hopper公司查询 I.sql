WITH recursive a1 AS
(
	SELECT  1 AS d
	UNION
	SELECT  d+1
	FROM a1
	WHERE d < 12 
) , a2 AS
(
	SELECT  1 AS d
	       ,driver_id
	FROM drivers
	WHERE join_date < '2020-01-31' 
	UNION ALL
	SELECT  month(join_date)
	       ,driver_id
	FROM drivers
	WHERE join_date > '2020-01-31'
	AND year(join_date) = 2020
) , a3 AS
(
	SELECT  d
	       ,SUM(case WHEN driver_id is null THEN 0 else 1 end) AS A
	FROM a1
	LEFT JOIN a2 using
	(d
	)
	GROUP BY  d
) , a4 AS
(
	SELECT  d
	       ,SUM(A)over(order by d)active
	FROM a3
)/*act*/
SELECT  *
FROM a4