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
SELECT  employee_id
       ,'Senior' experience
       ,ifnull(SUM(salary) OVER (),0) A
FROM a1
WHERE A <= 70000
UNION
SELECT  00 employee_id
       ,'0'experience
       ,'0'A)
SELECT  employee_id
FROM a2
WHERE A <= 70000-(
SELECT  A
FROM a3
ORDER BY A DESC
LIMIT 1 )
UNION
SELECT  employee_id
FROM a3
WHERE employee_id <> 00 