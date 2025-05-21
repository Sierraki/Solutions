SELECT  player_id
       ,device_id
FROM
(
	SELECT  player_id
	       ,device_id
	       ,event_date
	       ,rank() over(PARTITION BY player_id ORDER BY  event_date ASC) A
	FROM activity
)t1
WHERE A = 1