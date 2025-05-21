WITH recursive a1 AS
(
	SELECT  employee_id
	       ,manager_id
	       ,1 AS a
	FROM employees
	UNION ALL
	SELECT  a1.employee_id
	       ,e.manager_id
	       ,a+1
	FROM employees e
	JOIN a1
	ON a1.manager_id = e.employee_id
) , a2 AS
(
	SELECT  employee_id
	       ,COUNT(*) level
	FROM a1
	GROUP BY  employee_id
)/*level*/ , a3 AS (
SELECT  manager_id
       ,COUNT(*) team_size
FROM a1
WHERE manager_id is not null
GROUP BY  manager_id)/*size*/
         ,a4 AS (
SELECT  a1.manager_id
       ,SUM(salary) budget
FROM a1
LEFT JOIN employees e USING
(employee_id
)
WHERE a1.manager_id is not null
GROUP BY  a1.manager_id)/*budget*/
SELECT  employee_id
       ,employee_name
       ,level
       ,ifnull(team_size,0) team_size
       ,salary+ifnull(budget,0) budget
FROM a2
LEFT JOIN employees using
(employee_id
)
LEFT JOIN a3
ON a2.employee_id = a3.manager_id
LEFT JOIN a4
ON a2.employee_id = a4.manager_id
ORDER BY level, budget desc, employee_name