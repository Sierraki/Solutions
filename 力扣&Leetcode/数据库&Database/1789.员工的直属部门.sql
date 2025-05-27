SELECT  employee_id
       ,department_id
FROM
(
	SELECT  *
	FROM Employee
	WHERE primary_flag = 'y'
	UNION
	SELECT  distinct employee_id
	       ,department_id
	       ,primary_flag
	FROM Employee
)as t1
GROUP BY  employee_id