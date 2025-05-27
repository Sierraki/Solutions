WITH a1 AS
(
	SELECT  *
	       ,ROW_NUMBER()over(order by seat_id) A
	FROM cinema
	WHERE free = 1
) , a2 AS
(
	SELECT  *
	       ,COUNT(*)over(PARTITION BY seat_id-A) countt
	FROM a1
) , a3 AS
(
	SELECT  seat_id
	       ,free
	       ,countt
	       ,seat_id-ROW_NUMBER()over(order by seat_id) num
	FROM a2
	WHERE countt = (
	SELECT  MAX(countt)
	FROM a2 )
) , a4 AS
(
	SELECT  *
	       ,MIN(seat_id)over(PARTITION BY num) min
	       ,MAX(seat_id)over(PARTITION BY num) max
	       ,COUNT(*)over(PARTITION BY num) c
	FROM a3
)
SELECT  distinct min first_seat_id
       ,max last_seat_id
       ,c consecutive_seats_len
FROM a4
ORDER BY first_seat_id