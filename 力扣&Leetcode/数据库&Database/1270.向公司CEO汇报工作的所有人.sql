WITH a1 AS
(
	SELECT  e1.employee_id
	       ,e1.manager_id m1
	       ,e2.manager_id m2
	       ,e3.manager_id m3
	       ,e4.manager_id m4
	FROM Employees e1
	LEFT JOIN Employees e2
	ON e1.manager_id = e2.employee_id
	LEFT JOIN Employees e3
	ON e2.manager_id = e3.employee_id
	LEFT JOIN Employees e4
	ON e3.manager_id = e4.employee_id
), a2 as(
SELECT  employee_id
FROM a1
WHERE m4 <> 1)
SELECT  employee_id
FROM Employees
WHERE employee_id NOT IN ( SELECT * FROM a2 )
AND employee_id <> 1