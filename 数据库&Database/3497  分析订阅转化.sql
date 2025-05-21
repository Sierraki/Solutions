WITH a1 AS
(
	SELECT  user_id
	       ,activity_type
	       ,AVG(activity_duration) t
	FROM useractivity
	GROUP BY  user_id
	         ,activity_type
) , a2 AS
(
	SELECT  user_id
	       ,round(t,2) trial_avg_duration
	FROM a1
	WHERE activity_type = 'free_trial'
) , a3 AS
(
	SELECT  user_id
	       ,round(t,2) paid_avg_duration
	FROM a1
	WHERE activity_type = 'paid'
) , a4 AS
(
	SELECT  DISTINCT user_id
	FROM useractivity
) , a5 AS
(
	SELECT  user_id
	       ,trial_avg_duration
	       ,paid_avg_duration
	FROM a4
	LEFT JOIN a2 USING
	(user_id
	)
	LEFT JOIN a3 USING
	(user_id
	)
)
SELECT  *
FROM a5
WHERE paid_avg_duration is not NULL
AND trial_avg_duration is not NULL
ORDER BY user_id