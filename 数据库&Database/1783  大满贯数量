WITH a1 AS
(
	SELECT  Wimbledon id
	FROM Championships
	UNION ALL
	SELECT  Fr_open
	FROM Championships
	UNION ALL
	SELECT  US_open
	FROM Championships
	UNION ALL
	SELECT  Au_open
	FROM Championships
)
SELECT  id player_id
       ,player_name
       ,COUNT(*) grand_slams_count
FROM a1
JOIN players p
ON p.player_id = id
GROUP BY  id