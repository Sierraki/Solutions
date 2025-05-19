WITH t1 AS
(
	SELECT  student_id
	       ,course_id
	       ,grade
	       ,rank() OVER (PARTITION BY student_id ORDER BY  grade desc,course_id ASC) AS r
	FROM enrollments
)
SELECT  student_id
       ,course_id
       ,grade
FROM t1
WHERE r = 1