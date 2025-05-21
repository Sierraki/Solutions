WITH a1 AS
(
	SELECT  *
	       ,ROW_NUMBER()over(PARTITION BY student_id,subject ORDER BY  exam_date) A
	FROM scores
), a2 AS
(
	SELECT  *
	       ,ROW_NUMBER()over(PARTITION BY student_id,subject ORDER BY  exam_date DESC) B
	FROM scores
)
SELECT  a1.student_id
       ,a1.subject
       ,a1.score first_score
       ,a2.score latest_score
FROM a1
LEFT JOIN a2
ON a1.student_id = a2.student_id AND a1.subject = a2.subject
WHERE A = 1
AND B = 1
AND a2.score > a1.score
ORDER BY a1.student_id, a1.subject