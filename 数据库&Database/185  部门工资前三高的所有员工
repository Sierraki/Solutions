SELECT  d.name AS Department
       ,t2.Employee
       ,Salary
FROM
(
	SELECT  departmentId
	       ,name AS Employee
	       ,Salary
	FROM
	(
		SELECT  name
		       ,salary
		       ,departmentId
		       ,dense_rank() over(PARTITION BY departmentId ORDER BY  salary DESC ) AS ran
		FROM employee
	)t1
	WHERE ran <= 3
)t2, Department d
WHERE d.id = t2.departmentId 