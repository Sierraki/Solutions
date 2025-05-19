WITH t3 AS
(
	SELECT  fir_day AS install_dt
	       ,CASE WHEN activity.player_id is not null THEN 1  ELSE 0 END statu
	FROM
	(
		SELECT  player_id
		       ,fir_day
		       ,date_sub(fir_day,interval -1 day) AS next_day
		FROM
		(
			SELECT  player_id
			       ,MIN(event_date) AS fir_day
			FROM activity
			GROUP BY  player_id
		) tmp
	) t1
	LEFT JOIN activity
	ON t1.next_day = activity.event_date AND t1.player_id = activity.player_id
)
SELECT  install_dt
       ,COUNT(statu)                     AS installs
       ,round(SUM(statu)/COUNT(statu),2) AS Day1_retention
FROM t3
GROUP BY  install_dt