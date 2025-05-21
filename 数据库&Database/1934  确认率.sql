SELECT  s.user_id
       ,round(AVG(CAST( CASE WHEN c.action = 'confirmed' THEN 1 ELSE 0 END AS SIGNED) ),2)AS confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c
ON s.user_id = c.user_id
GROUP BY  s.user_id
ORDER BY  confirmation_rate ASC