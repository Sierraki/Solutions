WITH a1 AS
(
	SELECT  passenger_id
	       ,capacity
	       ,p.flight_id
	FROM Passengers p
	LEFT JOIN flights f
	ON p.flight_id = f.flight_id
) , a2 AS
(
	SELECT  *
	       ,COUNT(*) OVER (PARTITION BY flight_id) A
	FROM a1
) , a3 AS
(
	SELECT  distinct flight_id
	       ,if(A > capacity,capacity,A)booked_cnt
	       ,if(A-capacity < 0,0,A-capacity) waitlist_cnt
	FROM a2
)
SELECT  f.flight_id
       ,ifnull(booked_cnt,0)booked_cnt
       ,ifnull(waitlist_cnt,0)waitlist_cnt
FROM flights f
LEFT JOIN a3
ON a3.flight_id = f.flight_id
ORDER BY f.flight_id