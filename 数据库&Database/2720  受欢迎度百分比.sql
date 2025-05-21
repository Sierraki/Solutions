WITH a1 AS
(
	SELECT  user1
	       ,user2
	FROM friends
	UNION
	SELECT  user2
	       ,user1
	FROM friends
) , a2 as(
SELECT  user1
       ,COUNT(*) cnt
FROM a1
GROUP BY  user1)/*每个人的朋友数量*/
         ,a3 AS (
SELECT  distinct user1
       ,COUNT(*)over() total
FROM a1
GROUP BY  user1)/*用户名单*/
SELECT  user1
       ,round(cnt*100/total,2) percentage_popularity
FROM a3
LEFT JOIN a2 using
(user1
)
ORDER BY user1