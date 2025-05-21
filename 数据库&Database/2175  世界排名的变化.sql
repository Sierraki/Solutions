WITH a1 as
(
	SELECT  *
	       ,ROW_NUMBER() OVER (order by points desc,name ASC) rank1
	FROM teampoints
), /*before*/ a2 AS (
SELECT  a1.team_id
       ,a1.name
       ,a1.points+p.points_change pointt
FROM a1
LEFT JOIN PointsChange p
ON p.team_id = a1.team_id ), a3 AS
(
	SELECT  *
	       ,ROW_NUMBER() OVER (order by pointt desc,name ASC) rank2
	FROM a2
)/*after*/
SELECT  a1.team_id
       ,a1.name
       ,cast(rank1 AS char)-cast(rank2 AS char) rank_diff
FROM a1
LEFT JOIN a3
ON a1.team_id = a3.team_id