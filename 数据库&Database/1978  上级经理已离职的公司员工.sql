SELECT  employee_id
FROM employees
WHERE salary < 30000
AND manager_id is not null
AND manager_id NOT IN ( SELECT employee_id FROM employees )
ORDER BY employee_id asc