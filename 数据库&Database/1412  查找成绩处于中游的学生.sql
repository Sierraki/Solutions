WITH a1 AS
(
	SELECT  exam_id
	       ,student_id
	       ,score
	       ,rank() OVER (PARTITION BY exam_id ORDER BY  score DESC) AS ra1
	FROM exam
), a2 AS
(
	SELECT  exam_id
	       ,student_id
	       ,score
	       ,rank() OVER (PARTITION BY exam_id ORDER BY  score ASC) AS ra2
	FROM exam
), a3 AS
(
	SELECT  *
	FROM a1
	WHERE ra1 = 1 
	UNION ALL
	SELECT  *
	FROM a2
	WHERE ra2 = 1
), a4 AS
(
	SELECT  distinct student_id
	FROM Exam
)
SELECT  a4.student_id
       ,s.student_name
FROM a4
JOIN Student s
ON a4.student_id = s.student_id
WHERE a4.student_id NOT IN ( SELECT student_id FROM a3 ) 