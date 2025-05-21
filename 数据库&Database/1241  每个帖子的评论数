WITH a1 AS
(
	SELECT  distinct sub_id
	FROM submissions
	WHERE parent_id is null 
), a2 AS
(
	SELECT  sub_id
	       ,parent_id
	FROM submissions
	WHERE parent_id is not null 
), a3 AS
(
	SELECT  a1.sub_id id1
	       ,a2.sub_id id2
	FROM a1
	LEFT JOIN a2
	ON a1.sub_id = a2.parent_id
)
SELECT  id1 post_id
       ,COUNT(distinct id2) number_of_comments
FROM a3
GROUP BY  id1
ORDER BY  post_id asc