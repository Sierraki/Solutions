WITH temp1 AS
(
	SELECT  user_id1 AS user_id
	       ,user_id2 AS friend_id
	FROM Friends
	UNION ALL
	SELECT  user_id2
	       ,user_id1
	FROM Friends
)
SELECT  user_id1
       ,user_id2
FROM Friends
WHERE (user_id1, user_id2) NOT IN (
SELECT  t1.user_id   AS user_id1
       ,t1.friend_id AS user_id2
FROM temp1 AS t1, temp1 AS t2
WHERE t1.user_id != t2.user_id
AND t1.friend_id = t2.friend_id
AND (t1.user_id, t2.user_id) IN (
SELECT  *
FROM temp1))
ORDER BY user_id1, user_id2