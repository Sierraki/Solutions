WITH a AS
(
	SELECT  event_type
	       ,SUM(occurrences) / COUNT(business_id) AS avg_type
	FROM events
	GROUP BY  event_type
)
SELECT  distinct business_id
FROM events e
INNER JOIN a
ON e.event_type = a.event_type
WHERE occurrences > avg_type
GROUP BY  business_id
HAVING COUNT(*) >= 2