SELECT  distinct a.user1_id
       ,a.user2_id
FROM Friendship a, Listens b, Listens c
WHERE a.user1_id = b.user_id
AND a.user2_id = c.user_id
AND b.song_id = c.song_id
AND b.day = c.day
GROUP BY  a.user1_id
         ,a.user2_id
         ,b.day
HAVING COUNT(distinct b.song_id) >= 3