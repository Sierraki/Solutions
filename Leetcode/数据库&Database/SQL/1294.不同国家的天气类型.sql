SELECT  country_name
       ,CASE WHEN AVG(weather_state) <= 15 THEN 'Cold'
             WHEN AVG(weather_state) >= 25 THEN 'Hot'  ELSE 'Warm' END AS weather_type
FROM Weather w, Countries c
WHERE w.country_id = c.country_id
AND year(day) = 2019
AND month(day) = 11
GROUP BY  country_name