WITH a1 AS
(
	SELECT  team_name
	       ,wins*3+draws points
	       ,rank()over(order by wins*3+draws DESC) position
	       ,ROW_NUMBER()over(order by wins*3+draws desc,team_name) r
	FROM teamstats
	ORDER BY points desc, team_name
) , a2 AS
(
	SELECT  CEIL(COUNT(*)/3) 1st
	       ,COUNT(*)-ceil(COUNT(*)/3-1) 2rd
	FROM a1
), a3 AS
(
	SELECT  r
	       ,CASE WHEN r <= (
	SELECT  1st
	FROM a2 ) THEN 'Tier 1' WHEN r <= (
	SELECT  2rd
	FROM a2 )then 'Tier 2' else 'Tier 3' end AS 'tier'
	FROM a1
)
SELECT  team_name
       ,points
       ,position
       ,tier
FROM a1
LEFT JOIN a3
ON position = a3.r
ORDER BY points desc, team_name