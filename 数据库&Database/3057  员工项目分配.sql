WITH a1 AS
(
	SELECT  *
	FROM project
	LEFT JOIN employees using
	(employee_id
	)
) , a2 as(
SELECT  team
       ,AVG(workload) awl
FROM a1
GROUP BY  team)/*team avg work load*/
SELECT  EMPLOYEE_ID
       ,PROJECT_ID
       ,name EMPLOYEE_NAME
       ,workload PROJECT_WORKLOAD
FROM a1
LEFT JOIN a2 using
(team
)
WHERE workload > awl
ORDER BY employee_id, PROJECT_ID