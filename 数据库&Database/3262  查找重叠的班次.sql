WITH a1 AS
(
	SELECT  e1.employee_id
	       ,e1.start_time s1
	       ,e1.end_time e1
	       ,e2.start_time s2
	       ,e2.end_time e2
	FROM EmployeeShifts e1
	LEFT JOIN EmployeeShifts e2
	ON e1.employee_id = e2.employee_id
)
SELECT  employee_id
       ,COUNT(*)/2 overlapping_shifts
FROM a1
WHERE not( s1 = s2 AND e1 = e2 )
AND ( ( s1 BETWEEN s2 AND e2 )or ( e1 BETWEEN s2 AND e2 )or ( s2 BETWEEN s1 AND e1 )or ( e2 BETWEEN s1 AND e1 ) )
GROUP BY  employee_id