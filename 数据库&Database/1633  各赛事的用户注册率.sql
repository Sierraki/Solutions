SELECT  contest_id
       ,if (percentage >= 100,100,percentage) AS percentage
FROM
(
	SELECT  contest_id
	       ,round(COUNT(user_id)/(
	SELECT  COUNT(user_id)
	FROM users )*100, 2)as percentage
	FROM register
	GROUP BY  contest_id
	ORDER BY  percentage desc
	         ,contest_id ASC
)as t1