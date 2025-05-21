WITH t1 AS
(
	SELECT  home_team_id AS team_id
	FROM Matches
	UNION ALL
	SELECT  away_team_id AS team_id
	FROM Matches
), t2 AS
(
	SELECT  team_id
	       ,COUNT(1) AS matches_played
	FROM t1
	GROUP BY  team_id
), t3 AS
(
	SELECT  home_team_id                                                                           AS team_id
	       ,SUM(if(home_team_goals > away_team_goals,3,if(home_team_goals < away_team_goals,0,1))) AS home_points
	FROM Matches
	GROUP BY  home_team_id
), t4 AS
(
	SELECT  away_team_id                                                                           AS team_id
	       ,SUM(if(home_team_goals > away_team_goals,0,if(home_team_goals < away_team_goals,3,1))) AS away_points
	FROM Matches
	GROUP BY  away_team_id
), t5 AS
(
	SELECT  team_id
	       ,team_name
	       ,(ifnull(home_points,0) + ifnull(away_points,0)) AS points
	FROM Teams t
	LEFT JOIN t3 using
	(team_id
	)
	LEFT JOIN t4 using
	(team_id
	)
), t6 AS
(
	SELECT  home_team_id         AS team_id
	       ,SUM(home_team_goals) AS home_goal
	       ,SUM(away_team_goals) AS home_against_goal
	FROM Matches
	GROUP BY  home_team_id
), t7 AS
(
	SELECT  away_team_id         AS team_id
	       ,SUM(away_team_goals) AS away_goal
	       ,SUM(home_team_goals) AS away_against_goal
	FROM Matches
	GROUP BY  away_team_id
), t8 AS
(
	SELECT  team_id
	       ,team_name
	       ,(ifnull(home_goal,0) + ifnull(away_goal,0))                 AS goal_for
	       ,(ifnull(home_against_goal,0) + ifnull(away_against_goal,0)) AS goal_against
	FROM Teams t
	LEFT JOIN t6 using
	(team_id
	)
	LEFT JOIN t7 using
	(team_id
	)
)
SELECT  t5.team_name
       ,t2.matches_played
       ,t5.points
       ,t8.goal_for
       ,t8.goal_against
       ,(t8.goal_for - t8.goal_against) AS goal_diff
FROM t5
JOIN t2 using
(team_id
)
JOIN t8 using
(team_id, team_name
)
ORDER BY t5.points desc, goal_diff desc, team_name asc