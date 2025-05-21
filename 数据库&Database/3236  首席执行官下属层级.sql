WITH recursive a1 AS
(
	SELECT  employee_id
	       ,employee_name
	       ,manager_id
	FROM employees/*base*/
	UNION ALL
	SELECT  e1.employee_id
	       ,e1.employee_name
	       ,a1.manager_id
	FROM employees e1
	INNER JOIN a1
	ON a1.employee_id = e1.manager_id
) , a2 AS
(
	SELECT  employee_id subordinate_id
	       ,employee_name subordinate_name
	       ,COUNT(*) hierarchy_level
	FROM a1
	WHERE manager_id is not null
	GROUP BY  employee_id
) , a3 AS
(
	SELECT  employee_id
	FROM a1
	WHERE manager_id IN ( SELECT employee_id FROM employees WHERE manager_id is null )
)/*list*/
SELECT  subordinate_id
       ,subordinate_name
       ,hierarchy_level
       ,salary-(
SELECT  salary
FROM employees
WHERE manager_id is null ) salary_difference
FROM a2
LEFT JOIN employees e
ON e.employee_id = a2.subordinate_id
WHERE subordinate_id IN ( SELECT * FROM a3 )
ORDER BY hierarchy_level, subordinate_id