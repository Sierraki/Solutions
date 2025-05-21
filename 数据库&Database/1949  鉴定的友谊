WITH a AS
(
	SELECT  *
	FROM friendship
	UNION
	SELECT  user2_id
	       ,user1_id
	FROM friendship
)
SELECT  f.user1_id
       ,f.user2_id
       ,COUNT(*) AS common_friend
FROM friendship f
JOIN a t1
ON f.user1_id = t1.user1_id
JOIN a t2
ON f.user2_id = t2.user1_id AND t2.user2_id = t1.user2_id
GROUP BY  f.user1_id
         ,f.user2_id
HAVING COUNT(*) >= 3;