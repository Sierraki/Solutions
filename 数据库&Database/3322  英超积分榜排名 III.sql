SELECT  season_id
       ,team_id
       ,team_name
       ,3*wins+draws points
       ,goals_for-goals_against goal_difference
       ,ROW_NUMBER()over(PARTITION BY season_id ORDER BY  3*wins+draws desc,goals_for-goals_against desc,team_name) position
FROM SeasonStats
ORDER BY season_id, position, team_name