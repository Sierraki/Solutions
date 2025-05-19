SELECT  id
       ,visit_date
       ,people
FROM
(
	SELECT  id
	       ,visit_date
	       ,people
	       ,COUNT(id) over(PARTITION BY A) AS c
	FROM
	(
		SELECT  id
		       ,visit_date
		       ,people
		       ,id-ROW_NUMBER()over(order by id ASC) AS A
		FROM stadium
		WHERE people >= 100
		ORDER BY id ASC
	)t1
)t2
WHERE c >= 3
ORDER BY id asc