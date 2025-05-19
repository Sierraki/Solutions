SELECT  request_at       AS Day
       ,round(AVG(SS),2) AS 'Cancellation Rate'
FROM
(
	SELECT  driver_id
	       ,request_at
	       ,CASE WHEN status = 'completed'then 0  ELSE 1 END AS SS
	FROM trips
	WHERE client_id NOT IN ( SELECT users_id FROM  ( SELECT users_id FROM users WHERE banned = 'yes' )t1)
	AND driver_id NOT IN ( SELECT users_id FROM  ( SELECT users_id FROM users WHERE banned = 'yes' )t2)
)t3
GROUP BY  request_at
HAVING date(request_at) BETWEEN "2013-10-01"and "2013-10-03"