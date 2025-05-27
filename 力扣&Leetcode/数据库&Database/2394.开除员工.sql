WITH a1 AS
(
	SELECT  l.employee_id
	       ,SUM(ceil(timestampdiff(second,in_time,out_time)/60)) diff
	       ,needed_hours*60 A
	FROM logs l
	LEFT JOIN employees e
	ON e.employee_id = l.employee_id
	GROUP BY  employee_id
), a2 AS
(
	SELECT  e.employee_id
	       ,ifnull(diff,0) diff
	       ,A
	FROM Employees e
	LEFT JOIN a1
	ON e.employee_id = a1.employee_id
)
SELECT  employee_id
FROM a2
WHERE diff < A or diff = 0 