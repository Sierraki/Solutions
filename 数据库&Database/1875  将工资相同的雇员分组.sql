WITH a1 AS
(
	SELECT  *
	       ,COUNT(*) OVER (PARTITION BY salary) A
	FROM employees
)
SELECT  employee_id
       ,name
       ,salary
       ,dense_rank() OVER (order by salary) team_id
FROM a1
WHERE A >= 2
ORDER BY team_id, employee_id