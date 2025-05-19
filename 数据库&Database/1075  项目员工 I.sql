SELECT  project_id
       ,round(AVG(experience_years),2) AS average_years
FROM
(
	SELECT  project_id
	       ,experience_years
	FROM project, employee
	WHERE project.employee_id = employee.employee_id
) AS t1
GROUP BY  project_id