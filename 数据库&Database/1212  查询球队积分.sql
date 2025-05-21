WITH h1 AS
(
	SELECT  host_team team
	       ,CASE WHEN host_goals > guest_goals THEN 3
	             WHEN host_goals < guest_goals THEN 0  ELSE 1 END AS p
	FROM Matches
), g1 AS
(
	SELECT  guest_team team
	       ,CASE WHEN host_goals > guest_goals THEN 0
	             WHEN host_goals < guest_goals THEN 3  ELSE 1 END AS p
	FROM Matches
), t1 AS
(
	SELECT  team
	       ,p
	FROM h1
	UNION ALL
	SELECT  team
	       ,p
	FROM g1
), t2 AS
(
	SELECT  team
	       ,SUM(p) A
	FROM t1
	GROUP BY  team
)
SELECT  t.team_id
       ,t.team_name
       ,ifnull (A,0) AS num_points
FROM teams t
LEFT JOIN t2
ON t.team_id = t2.team
ORDER BY num_points desc, t.team_id asc