WITH a1 AS
(
	SELECT  DISTINCT post_id
	       ,IFNULL(topic_id,'Ambiguous!') AS topic_id
	FROM Posts p
	LEFT JOIN Keywords k
	ON content LIKE CONCAT('%', ' ', word, '%') OR content LIKE CONCAT('%', ' ', word, ' ', '%') OR content LIKE CONCAT('%', word, ' ', '%')
)
SELECT  post_id
       ,GROUP_CONCAT( topic_id ORDER BY  CASE WHEN topic_id = 'Ambiguous!' THEN 1 ELSE 0 END,CAST(topic_id AS UNSIGNED) -- 按数字排序 
 ) AS topic
FROM a1
GROUP BY  post_id;