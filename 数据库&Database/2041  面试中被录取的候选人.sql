WITH a1 AS
(
	SELECT  interview_id
	       ,SUM(score) score
	FROM rounds
	GROUP BY  interview_id
)
SELECT  c.candidate_id
FROM candidates c
LEFT JOIN a1
ON c.interview_id = a1.interview_id
WHERE years_of_exp >= 2
AND score > 15