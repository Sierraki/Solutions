SELECT  d.name  AS Department
       ,t2.name AS Employee
       ,t2.Salary
FROM
(
	SELECT  name
	       ,Salary
	       ,departmentId
	FROM
	(
		SELECT  name
		       ,salary
		       ,departmentId
		       ,RANK() OVER (PARTITION BY departmentId ORDER BY  salary DESC) AS AA
		FROM employee
	)t1
	WHERE AA = 1
)t2, department d
WHERE d.id = t2.departmentId