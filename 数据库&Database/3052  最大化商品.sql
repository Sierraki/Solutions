WITH a1 AS
(
	SELECT  item_type
	       ,SUM(square_footage) SS
	       ,COUNT(*)cnt
	FROM inventory
	GROUP BY  item_type
) , a2 AS
(
	SELECT  item_type
	       ,FLOOR(500000/SS)*cnt item_count
	FROM a1
	WHERE item_type = 'prime_eligible'
)/*prime*/ , a3 AS (
SELECT  *
       ,500000-SS*floor(500000/SS) lef
FROM a1
WHERE item_type = 'prime_eligible')
SELECT  item_type
       ,FLOOR((
SELECT  lef
FROM a3 )/SS)*cnt item_count
FROM a1
WHERE item_type = 'not_prime'
UNION
SELECT  *
FROM a2
ORDER BY item_count DESC