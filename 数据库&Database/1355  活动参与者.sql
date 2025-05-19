WITH a1 AS
(
	SELECT  activity
	       ,COUNT(*) AS A
	FROM Friends
	GROUP BY  activity
)
SELECT  activity
FROM a1
WHERE A NOT IN ( SELECT MIN (A) FROM a1 UNION  SELECT MAX(A) FROM a1 ); 