WITH a1 AS
(
	SELECT  r1.user_id id1
	       ,r2.user_id id2
	       ,r1.follower_id f
	       ,dense_rank() OVER (PARTITION BY r1.user_id,r2.user_id ORDER BY  r1.follower_id) A
	FROM relations r1, relations r2
	WHERE r1.follower_id = r2.follower_id
	AND r1.user_id <> r2.user_id
	ORDER BY r1.user_id
), a2 AS
(
	SELECT  id1
	       ,id2
	       ,dense_rank() OVER (order by A DESC) r
	FROM a1
	WHERE id1 <= id2
	ORDER BY A DESC
)
SELECT  id1 user1_id
       ,id2 user2_id
FROM a2
WHERE r = 1