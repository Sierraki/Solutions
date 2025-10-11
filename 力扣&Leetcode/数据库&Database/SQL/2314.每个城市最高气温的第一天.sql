WITH a1 AS
(
	SELECT  *
	       ,ROW_NUMBER() OVER (PARTITION BY city_id ORDER BY  degree desc,day ASC) A
	FROM weather
)
SELECT  city_id
       ,day
       ,degree
FROM a1
WHERE A = 1
ORDER BY city_id 