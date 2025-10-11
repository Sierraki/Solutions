WITH a1 AS
(
	SELECT  school_id
	       ,capacity
	       ,score
	       ,ROW_NUMBER() over(PARTITION BY school_id ORDER BY  score ) r
	FROM schools, exam
	WHERE capacity >= student_count
)
SELECT  school_id
       ,score
FROM a1
WHERE r = 1
UNION
SELECT  school_id
       ,-1
FROM schools
WHERE school_id NOT IN ( SELECT school_id FROM a1 )