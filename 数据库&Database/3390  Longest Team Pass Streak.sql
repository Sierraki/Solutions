# Write your MySQL query statement below
WITH tmp AS
(
	SELECT  SUM(t1.team_name != t2.team_name) OVER (PARTITION BY t1.team_name ORDER BY  p.time_stamp) s
	       ,t1.team_name team_name
	FROM passes p
	JOIN teams t1
	ON p.pass_from = t1.player_id
	JOIN teams t2
	ON p.pass_to = t2.player_id
) , tmp2 AS
(
	SELECT  team_name
	       ,CASE WHEN s = 0 THEN COUNT(*)  ELSE COUNT(*)-1 END cnt
	FROM tmp
	GROUP BY  team_name
	         ,s
	HAVING cnt != 0
)
SELECT  team_name
       ,MAX(cnt) longest_streak
FROM tmp2
GROUP BY  team_name
ORDER BY  team_name