WITH a1 AS
(
	SELECT  *
	       ,ROW_NUMBER() OVER (order by player_id,match_day) num
	FROM matches
), a2 AS
(
	SELECT  *
	       ,ROW_NUMBER() OVER (PARTITION BY player_id,result ORDER BY  match_day) A
	FROM a1
), a3 AS
(
	SELECT  player_id
	       ,match_day
	       ,num
	       ,num-A
	       ,COUNT(*) OVER (PARTITION BY player_id,num-A) wincount
	FROM a2
	WHERE result = 'Win' 
), a4 AS
(
	SELECT  player_id
	       ,wincount
	       ,ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY  wincount DESC) rankk
	FROM a3
), a5 AS
(
	SELECT  player_id
	       ,wincount
	FROM a4
	WHERE rankk = 1 
)
SELECT  distinct m.player_id
       ,ifnull(wincount,0) longest_streak
FROM matches m
LEFT JOIN a5
ON m.player_id = a5.player_id