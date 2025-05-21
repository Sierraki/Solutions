WITH a1 AS
(
	SELECT  log_id
	       ,ip
	       ,substring_index(ip,'.',1) 1st
	       ,substring_index(substring_index(ip,'.',2),'.',-1) 2rd
	       ,substring_index(substring_index(ip,'.',3),'.',-1) 3th
	       ,substring_index(ip,'.',-1) 4th
	FROM logs
)
SELECT  ip
       ,COUNT(*)invalid_count
FROM a1
WHERE ip not regexp '^[^.]+\\.[^.]+\\.[^.]+\\.[^.]+$' or 1st > 255 or 2rd > 255 or 3th > 255 or 4th > 255 or left(1st, 1) = 0 or left(2rd, 1) = 0 or left(3th, 1) = 0 or left(4th, 1) = 0
GROUP BY  ip
ORDER BY  invalid_count desc
         ,ip desc