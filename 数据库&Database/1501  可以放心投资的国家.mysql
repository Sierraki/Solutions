WITH a1 AS
(
	SELECT  id
	       ,c.name
	FROM Person p
	LEFT JOIN Country c
	ON left(p.phone_number, 3) = c.country_code
), a2 AS
(
	SELECT  caller_id A
	       ,callee_id B
	       ,duration
	FROM Calls
), a3 AS
(
	SELECT  callee_id A
	       ,caller_id B
	       ,duration
	FROM Calls
), t1 AS
(
	SELECT  *
	FROM a2
	UNION ALL
	SELECT  *
	FROM a3
), a4 AS
(
	SELECT  AVG(duration) AB
	FROM t1, a1
	WHERE t1.A = a1.id 
), a5 AS
(
	SELECT  name
	       ,AVG(duration) ABC
	FROM t1, a1
	WHERE t1.A = a1.id
	GROUP BY  name
)
SELECT  name country
FROM a5
CROSS JOIN a4
WHERE ABC > AB 