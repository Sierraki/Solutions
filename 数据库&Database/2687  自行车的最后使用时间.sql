WITH a1 AS
(
	SELECT  *
	       ,ROW_NUMBER() OVER (PARTITION BY bike_number ORDER BY  end_time DESC ) r
	FROM bikes
)
SELECT  bike_number
       ,end_time
FROM a1
WHERE r = 1
ORDER BY end_time desc