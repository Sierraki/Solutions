WITH a1 AS
(
	SELECT  *
	       ,rank() OVER (PARTITION BY department_id ORDER BY  mark DESC) rankk
	       ,COUNT(*) OVER (PARTITION BY department_id) countt
	FROM students
)
SELECT  student_id
       ,department_id
       ,round(ifnull((rankk-1)*100/(countt-1),0),2) percentage
FROM a1