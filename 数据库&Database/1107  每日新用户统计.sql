WITH a1 AS
(
	SELECT  *
	       ,ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY  activity_date ASC) A
	FROM traffic
	WHERE activity = 'login' 
), a2 AS
(
	SELECT  user_id
	       ,activity
	       ,activity_date
	FROM a1
	WHERE A = 1
	AND activity_date BETWEEN date_sub( '2019-06-30', interval 90 day) AND '2019-06-30' 
)
SELECT  activity_date login_date
       ,COUNT(*) user_count
FROM a2
GROUP BY  activity_date