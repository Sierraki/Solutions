SELECT  project_id
FROM
(
	SELECT  project_id
	       ,rank() OVER (order by COUNT(employee_id) DESC) r
	FROM project
	GROUP BY  project_id
)t1
WHERE r = 1