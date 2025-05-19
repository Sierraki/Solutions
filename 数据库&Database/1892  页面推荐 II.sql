WITH a1 AS
(
	SELECT  user1_id id1
	       ,user2_id id2
	FROM friendship
	UNION ALL
	SELECT  user2_id
	       ,user1_id
	FROM friendship
	ORDER BY id1
), a2 AS
(
	SELECT  id1
	       ,id2
	       ,l2.page_id p2
	FROM a1
	LEFT JOIN likes l2
	ON l2.user_id = id2
), a3 AS
(
	SELECT  id1
	       ,id2
	       ,p2
	FROM a2
	WHERE not exists (
	SELECT  1
	FROM likes l
	WHERE a2.id1 = l.user_id
	AND l.page_id = a2. p2 )
)
SELECT  distinct id1 user_id
       ,p2 page_id
       ,COUNT(*) OVER (PARTITION BY id1,p2) friends_likes
FROM a3