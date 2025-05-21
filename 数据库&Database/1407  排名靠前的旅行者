SELECT  u.name
       ,ifnull(t1.travelled_distance,0)as travelled_distance
FROM users u
LEFT JOIN
(
	SELECT  *
	       ,SUM(distance) AS travelled_distance
	FROM rides r
	GROUP BY  user_id
	ORDER BY  travelled_distance DESC
) AS t1
ON u.id = t1.user_id
ORDER BY travelled_distance desc, name asc