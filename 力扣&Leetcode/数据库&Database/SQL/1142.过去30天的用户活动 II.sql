WITH a1 AS
(
	SELECT  user_id
	       ,COUNT(DISTINCT session_id) A
	FROM activity
	WHERE activity_date BETWEEN date_sub('2019-07-27', interval 29 day) AND '2019-07-27'
	GROUP BY  user_id
)
SELECT  ifnull(round(AVG(A),2),0) average_sessions_per_user
FROM a1