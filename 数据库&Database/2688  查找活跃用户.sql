WITH a1 AS
(
	SELECT  user_id
	       ,created_at
	       ,timestampdiff(day,lag(created_at) OVER (PARTITION BY user_id ORDER BY  created_at ),created_at) diff
	FROM users
)
SELECT  distinct user_id
FROM a1
WHERE diff <= 7
ORDER BY user_id