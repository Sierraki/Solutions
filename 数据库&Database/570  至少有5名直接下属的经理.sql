SELECT  name
FROM
(
	SELECT  managerid
	FROM employee
	GROUP BY  managerid
	HAVING managerid is not null AND COUNT(department) >= 5
)as t1
JOIN employee
WHERE employee.id = t1.managerid