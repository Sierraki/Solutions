SELECT  t1.name follower
       ,follow_cum num
FROM
(
	SELECT  followee AS name
	       ,COUNT(*)as follow_cum
	FROM follow
	GROUP BY  followee
	HAVING COUNT(*) >= 1
)t1
INNER JOIN
(
	SELECT  follower AS name
	       ,COUNT(*)as followee_cum
	FROM follow
	GROUP BY  follower
	HAVING COUNT(*) >= 1
)t2
ON t1.name = t2.name
ORDER BY follower asc