WITH a1 AS
(
	SELECT  employee_id id
	       ,start_time st
	FROM EmployeeShifts
	UNION ALL
	SELECT  employee_id id
	       ,end_time
	FROM EmployeeShifts
) , a2 AS
(
	SELECT  id
	       ,st
	       ,lead(st)over(PARTITION BY id ORDER BY  st) e
	       ,end_time
	       ,ROW_NUMBER()over(PARTITION BY id ORDER BY st) num
	       ,ROW_NUMBER()over(PARTITION BY id,(end_time is not null)order by st) num1
	FROM a1
	LEFT JOIN EmployeeShifts e
	ON a1.id = e.employee_id AND e.start_time = a1.st
	ORDER BY id, st
) , a3 AS
(
	SELECT  *
	       ,COUNT(*)over(PARTITION BY id,num-num1) cnt
	FROM a2
	WHERE st <= e
	AND e <= end_time
) , a4 as(
SELECT  id
       ,MAX(cnt) max_overlapping_shifts
FROM a3
GROUP BY  id/*maxxxxxxxx*/)
         ,a5 AS
(
	SELECT  e1.employee_id id
	       ,e1.start_time s1
	       ,e1.end_time e1
	       ,e2.start_time s2
	       ,e2.end_time e2
	FROM EmployeeShifts e1
	CROSS JOIN EmployeeShifts e2
	ON e1.employee_id = e2.employee_id where( e1.start_time, e1.end_time ) <> ( e2.start_time, e2.end_time )
	ORDER BY id, s1
) , a6 AS
(
	SELECT  *
	       ,(case WHEN e1 <= s2 THEN 0 WHEN e2 <= s1 THEN 0 WHEN s1 <= s2 AND e2 <= e1 THEN timestampdiff(minute,s2,e2) WHEN s2 <= s1 AND e1 <= e2 THEN timestampdiff(minute,s1,e1) WHEN s1 <= s2 AND e1 <= e2 THEN timestampdiff(minute,s2,e1) WHEN s2 <= s1 AND e2 <= e1 THEN timestampdiff(minute,s1,e2) end ) AS dur
	FROM a5
) , a7 AS
(
	SELECT  id
	       ,SUM(dur)/2 total_overlap_duration
	FROM a6
	GROUP BY  id/*total*/
) /*select id employee_id, max_overlapping_shifts, ifnull(total_overlap_duration, 0)total_overlap_duration
FROM a4
LEFT JOIN a7 using
(id
)
ORDER BY employee_id*/
SELECT  *
FROM a4