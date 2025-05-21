WITH a1 AS
(
	SELECT  user1_id id1
	       ,user2_id id2
	FROM friendship
	UNION ALL
	SELECT  user2_id id1
	       ,user1_id id2
	FROM friendship
), a2 AS
(
	SELECT  *
	FROM Likes
	WHERE user_id = 1 
), a3 AS
(
	SELECT  distinct page_id
	FROM a1
	JOIN Likes l
	ON a1.id2 = l.user_id
	WHERE id1 = 1 
)
SELECT  page_id AS recommended_page
FROM a3
WHERE page_id NOT IN ( SELECT page_id FROM a2 ) 