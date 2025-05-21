WITH L AS
(
	SELECT  user_id
	       ,song_id
	       ,day
	FROM Listens
	GROUP BY  user_id
	         ,song_id
	         ,day
), T AS
(
	SELECT  L1.user_id AS u1_id
	       ,L2.user_id AS u2_id
	       ,L1.day
	       ,L1.song_id
	FROM L L1, L L2
	WHERE L1.day = L2.day
	AND L1.song_id = L2.song_id
	AND L1.user_id < L2.user_id 
), D AS
(
	SELECT  u1_id
	       ,u2_id
	       ,day
	FROM T
	GROUP BY  u1_id
	         ,u2_id
	         ,day
	HAVING COUNT(*) >= 3
), ANS AS
(
	SELECT  u1_id
	       ,u2_id
	FROM D
	GROUP BY  u1_id
	         ,u2_id EXCEPT
	SELECT  *
	FROM Friendship
)
SELECT  u1_id AS user_id
       ,u2_id AS recommended_id
FROM ANS
UNION
SELECT  u2_id
       ,u1_id
FROM ANS EXCEPT
SELECT  user2_id
       ,user1_id
FROM Friendship