SELECT  project_id
       ,employee_id
FROM
(
	SELECT  p.project_id
	       ,p.employee_id
	       ,rank() OVER (PARTITION BY p.project_id ORDER BY  experience_years DESC) AS r
	FROM project p
	LEFT JOIN Employee e
	ON p.employee_id = e.employee_id
)t1
WHERE r = 1