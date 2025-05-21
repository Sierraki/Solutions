WITH a1 AS
(
	SELECT  *
	       ,rank() OVER (PARTITION BY emp_id ORDER BY  Salary DESC) r
	FROM Salary
)
SELECT  emp_id
       ,firstname
       ,lastname
       ,salary
       ,department_id
FROM a1
WHERE r = 1
ORDER BY emp_id