SELECT  id
       ,month
       ,salary
FROM
(
	SELECT  *
	       ,rank() over(PARTITION BY id ORDER BY  month DESC) AS c
	FROM
	(
		SELECT  id
		       ,month
		       ,SUM(salary)over(PARTITION BY id,aa ORDER BY  month DESC rows BETWEEN current row AND 2 following) AS salary
		FROM
		(
			SELECT  *
			       ,month-num AS aa
			FROM
			(
				SELECT  id
				       ,month
				       ,salary
				       ,ROW_NUMBER()over(PARTITION BY id ORDER BY  month ASC) AS num
				FROM employee
			)t1
		)t2
		ORDER BY id, month DESC
	)t3
)t4
WHERE c <> 1