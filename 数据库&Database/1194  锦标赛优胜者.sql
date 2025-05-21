WITH a1 AS
(
	SELECT  first_player p1
	       ,second_player p2
	       ,first_score s1
	       ,second_score s2
	FROM Matches
	UNION ALL
	SELECT  second_player
	       ,first_player
	       ,second_score
	       ,first_score
	FROM Matches
), a2 AS
(
	SELECT  p1
	       ,SUM(s1) sc
	       ,group_id
	FROM a1
	LEFT JOIN players
	ON p1 = player_id
	GROUP BY  p1
), a3 AS
(
	SELECT  group_id
	       ,p1
	       ,sc
	       ,ROW_NUMBER() OVER (PARTITION BY group_id ORDER BY  sc desc,p1 ASC) rr
	FROM a2
)
SELECT  group_id
       ,p1 player_id
FROM a3
WHERE rr = 1