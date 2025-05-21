WITH a1 AS
(
	SELECT  view_date
	       ,viewer_id
	       ,COUNT( distinct article_id) A
	FROM views
	GROUP BY  view_date
	         ,viewer_id
)
SELECT  distinct viewer_id id
FROM a1
WHERE A >= 2
ORDER BY viewer_id