WITH a1 AS
(
	SELECT  voter
	       ,1/COUNT(*) p
	FROM votes
	WHERE candidate is not null
	GROUP BY  voter
) , a2 AS
(
	SELECT  v.candidate
	       ,SUM(p) A
	FROM Votes v
	LEFT JOIN a1
	ON a1.voter = v.voter
	WHERE candidate is not null
	GROUP BY  candidate
) , a3 AS
(
	SELECT  candidate
	       ,A
	       ,rank() OVER (order by A DESC) r
	FROM a2
)
SELECT  candidate
FROM a3
WHERE r = 1
ORDER BY candidate 