SELECT  user_id
       ,COUNT(distinct follower_id) AS followers_count
FROM followers
GROUP BY  user_id