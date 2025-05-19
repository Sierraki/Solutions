WITH a1 AS
(
	SELECT  team_id
	       ,team_name
	       ,wins*3+draws*1 points
	FROM teamstats
)
SELECT  *
       ,rank()over(order by points DESC) position
FROM a1
ORDER BY position, team_name