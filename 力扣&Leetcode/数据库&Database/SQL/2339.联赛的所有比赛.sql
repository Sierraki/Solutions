SELECT  t1.team_name home_team
       ,t2.team_name away_team
FROM teams t1 , teams t2
WHERE t1.team_name <> t2.team_name