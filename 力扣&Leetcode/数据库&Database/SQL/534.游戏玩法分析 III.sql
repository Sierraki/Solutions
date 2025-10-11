SELECT  player_id
       ,event_date
       ,SUM(games_played) over(PARTITION BY player_id ORDER BY  event_date ASC) games_played_so_far
FROM activity