WITH a1 AS
(
	SELECT  'A'
	       ,COUNT(*) N
	FROM newyork
	WHERE score >= 90 
), a2 AS
(
	SELECT  'A'
	       ,COUNT(*) Y
	FROM California
	WHERE score >= 90 
)
SELECT  CASE WHEN Y = N THEN 'No Winner'
             WHEN Y < N THEN 'New York University'  ELSE 'California University' END AS 'winner'
FROM a1, a2