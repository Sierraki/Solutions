WITH a1 as
(
	SELECT  user_id
	       ,SUM(distance)total
	FROM rides
	GROUP BY  user_id
)
SELECT  u.user_id
       ,name
       ,ifnull(total,0) AS 'traveled distance'
FROM users u
LEFT JOIN a1
ON u.user_id = a1.user_id
ORDER BY u.user_id