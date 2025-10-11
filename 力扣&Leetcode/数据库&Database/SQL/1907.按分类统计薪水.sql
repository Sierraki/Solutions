SELECT  t1.category
       ,ifnull(t2.accounts_count,0)as accounts_count
FROM
(
	SELECT  'Low Salary'as category
	UNION
	SELECT  'Average Salary'as category
	UNION
	SELECT  'High Salary'as category
)as t1
LEFT JOIN
(
	SELECT  CASE WHEN income < 20000 THEN 'Low Salary'
	             WHEN income > 50000 THEN 'High Salary'
	             WHEN income BETWEEN 20000 AND 50000 THEN 'Average Salary'  ELSE null END AS category
	       ,COUNT(income)                                                                 AS accounts_count
	FROM accounts
	GROUP BY  category
)as t2
ON t1.category = t2.category