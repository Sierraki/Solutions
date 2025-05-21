WITH a1 AS
(
	SELECT  departure_airport
	       ,arrival_airport
	       ,flights_count
	FROM flights
	UNION
	SELECT  arrival_airport
	       ,departure_airport
	       ,flights_count
	FROM flights
), a2 AS
(
	SELECT  departure_airport
	       ,rank() OVER (order by SUM(flights_count) DESC ) r
	FROM a1
	GROUP BY  departure_airport
)
SELECT  departure_airport airport_id
FROM a2
WHERE r = 1