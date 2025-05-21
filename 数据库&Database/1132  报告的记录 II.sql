WITH a AS
(
	SELECT  a.action_date
	       ,a.post_id
	       ,a.extra
	       ,r.remove_date
	FROM actions a
	LEFT JOIN removals r
	ON a.post_id = r.post_id
	WHERE action = "report"
	AND extra = "spam" 
)
SELECT  round(AVG(num) * 100,2) AS average_daily_percent
FROM
(
	SELECT  COUNT(distinct (case whenremove_date is not null THEN post_id end)) / COUNT(distinct post_id) AS num
	FROM a
	GROUP BY  action_date
) AS b