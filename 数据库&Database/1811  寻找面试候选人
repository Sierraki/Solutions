WITH a1 AS
(
	SELECT  gold_medal id
	FROM contests
	GROUP BY  gold_medal
	HAVING COUNT(*) >= 3
), /*三金甚至更多*/ a2 AS (
SELECT  contest_id id
       ,gold_medal m
FROM contests
UNION ALL
SELECT  contest_id
       ,silver_medal
FROM contests
UNION ALL
SELECT  contest_id
       ,bronze_medal
FROM contests), a3 AS
(
	SELECT  m
	       ,id
	       ,ROW_NUMBER() OVER (PARTITION BY m ORDER BY  id ASC) A
	       ,id-ROW_NUMBER() OVER (PARTITION BY m ORDER BY id ASC) B
	FROM a2
), a4 AS
(
	SELECT  m
	       ,B
	       ,COUNT(*) OVER (PARTITION BY m,B) C
	FROM a3
), a5 AS
(
	SELECT  distinct m
	FROM a4
	WHERE C >= 3 
	UNION ALL
	SELECT  *
	FROM a1
)
SELECT  distinct name
       ,mail
FROM a5
LEFT JOIN users u
ON u.user_id = m