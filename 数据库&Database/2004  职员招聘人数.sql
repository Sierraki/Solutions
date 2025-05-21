WITH a1 AS
(
	SELECT  *
	       ,SUM(salary) OVER (rows BETWEEN unbounded preceding AND current row) A
	FROM Candidates
	WHERE experience = 'Senior'
	ORDER BY salary ASC
), /*资深*/ a2 AS (
SELECT  *
       ,SUM(salary) OVER (rows BETWEEN unbounded preceding AND current row) A
FROM Candidates
WHERE experience = 'Junior'
ORDER BY salary ASC), /*新手*/ a3 AS (
SELECT  'Senior' experience
       ,COUNT(*) accepted_candidates
       ,ifnull(SUM(salary),0) A
FROM a1
WHERE A <= 70000)
SELECT  'Junior' experience
       ,COUNT(*) accepted_candidates
FROM a2
WHERE A <= 70000-(
SELECT  A
FROM a3 )
UNION
SELECT  experience
       ,accepted_candidates
FROM a3