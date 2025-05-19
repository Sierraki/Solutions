WITH a1 AS
(
	SELECT  *
	       ,COUNT(*)over(PARTITION BY flight_id ORDER BY  booking_time) state
	FROM passengers
	LEFT JOIN flights using
	(flight_id
	)
)
SELECT  passenger_id
       ,CASE WHEN state <= capacity THEN 'Confirmed'  ELSE 'Waitlist' END AS Status
FROM a1
ORDER BY passenger_id