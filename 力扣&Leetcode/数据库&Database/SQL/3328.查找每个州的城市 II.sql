WITH a1 AS
(
	SELECT  state
	       ,COUNT(*) sc
	FROM cities
	WHERE left(state, 1) = left(city, 1)
	GROUP BY  state
) /*字母相同*/ , a2 AS (
SELECT  state
FROM cities
GROUP BY  state
HAVING COUNT(*) >= 3) /*至少有三个城市*/ , a3 as(
SELECT  *
FROM a1
WHERE state IN ( SELECT state FROM a2 ))/*final*/
SELECT  a3.state
       ,group_concat(c.city ORDER BY  c.city separator', ' ) cities
       ,sc matching_letter_count
FROM cities c
LEFT JOIN a3
ON c.state = a3.state
WHERE c.state IN ( SELECT state FROM a3 )
GROUP BY  state
ORDER BY  matching_letter_count desc
         ,state