WITH a1 AS
(
	SELECT  *
	       ,dense_rank() OVER (PARTITION BY dept ORDER BY  salary DESC) r
	FROM employees
)
SELECT  emp_id
       ,dept
FROM a1
WHERE r = 2
ORDER BY emp_id