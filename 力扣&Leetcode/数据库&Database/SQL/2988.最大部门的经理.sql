WITH a1 AS
(
	SELECT  dep_id
	       ,COUNT(*) countt
	FROM employees
	GROUP BY  dep_id
), a2 AS
(
	SELECT  *
	       ,rank() over(order by countt DESC) rankk
	FROM a1
)
SELECT  emp_name manager_name
       ,dep_id
FROM Employees
WHERE dep_id IN ( SELECT dep_id FROM a2 WHERE rankk = 1 )
AND position = 'manager'
ORDER BY dep_id