SELECT  c.name
FROM
(
	SELECT  candidateId
	       ,COUNT(*)as A
	FROM vote
	GROUP BY  candidateId
)t1, Candidate c
WHERE c.id = t1.candidateId
ORDER BY t1.A DESC
LIMIT 1