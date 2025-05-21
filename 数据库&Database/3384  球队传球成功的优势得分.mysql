WITH a1 AS
(
	SELECT  t1.team_name fid
	       ,p.pass_from
	       ,p.time_stamp
	       ,p.pass_to
	       ,t2.team_name tid
	FROM passes p
	LEFT JOIN teams t1
	ON t1.player_id = p.pass_from
	LEFT JOIN teams t2
	ON t2.player_id = p.pass_to
) , a2 AS
(
	SELECT  fid team_name
	       ,SUM(case WHEN fid = tid THEN 1 else -1 end )as dominance
	FROM a1
	WHERE time_stamp <= '45:00'
	GROUP BY  fid
)/*shang ban chang */ , a3 AS (
SELECT  fid team_name
       ,SUM(case WHEN fid = tid THEN 1 else -1 end )as dominance
FROM a1
WHERE time_stamp > '45:00'
GROUP BY  fid)/*xia ban chang */
SELECT  team_name
       ,1 AS half_number
       ,dominance
FROM a2
UNION ALL
SELECT  team_name
       ,2 AS half_number
       ,dominance
FROM a3
ORDER BY team_name, half_number