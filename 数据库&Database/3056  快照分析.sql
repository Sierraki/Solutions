WITH a1 AS
(
	SELECT  age_bucket
	       ,activity_type
	       ,time_spent
	FROM Activities
	LEFT JOIN age using
	(user_id
	)
) , a2 AS
(
	SELECT  age_bucket
	       ,SUM(time_spent) ot
	FROM a1
	WHERE activity_type = 'open'
	GROUP BY  age_bucket
) , a3 AS
(
	SELECT  age_bucket
	       ,SUM(time_spent) st
	FROM a1
	WHERE activity_type = 'send'
	GROUP BY  age_bucket
) , a4 AS
(
	SELECT  age_bucket
	       ,round(st*100/(ot+st),2)send_perc
	       ,100-round(st*100/(ot+st),2) open_perc
	FROM a2
	LEFT JOIN a3 using
	(age_bucket
	)
)
SELECT  distinct age_bucket
       ,ifnull(send_perc,100)send_perc
       ,ifnull(open_perc,0)open_perc
FROM age
LEFT JOIN a4 using
(age_bucket
)