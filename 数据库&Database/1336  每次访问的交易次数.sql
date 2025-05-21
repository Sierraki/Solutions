WITH recursive a1 AS
(
	SELECT  0 AS cnt
	UNION
	SELECT  cnt+1
	FROM a1
	WHERE cnt < (
	SELECT  MAX(cnt)
	FROM
	(
		SELECT  v.user_id
		       ,v.visit_date
		       ,SUM(case WHEN t.user_id is not null THEN 1 else 0 end) AS cnt
		FROM visits v
		LEFT JOIN transactions t
		ON v.user_id = t.user_id AND transaction_date = visit_date
		GROUP BY  v.user_id
		         ,visit_date
	)t1 )
) , a2 AS
(
	SELECT  v.user_id
	       ,v.visit_date
	       ,SUM(case WHEN t.user_id is not null THEN 1 else 0 end) AS cnt
	FROM visits v
	LEFT JOIN transactions t
	ON v.user_id = t.user_id AND transaction_date = visit_date
	GROUP BY  v.user_id
	         ,visit_date
) , a3 AS
(
	SELECT  cnt
	       ,COUNT(*) visits_count
	FROM a2
	GROUP BY  cnt
)
SELECT  cnt transactions_count
       ,ifnull(visits_count,0)visits_count
FROM a1
LEFT JOIN a3 USING
(cnt
)
ORDER BY transactions_count