SELECT  u.user_id AS buyer_id
       ,join_date
       ,ifnull(t2.orders_in_2019,0)as orders_in_2019
FROM
(
	SELECT  buyer_id
	       ,COUNT(order_date)as orders_in_2019
	FROM
	(
		SELECT  order_date
		       ,buyer_id
		FROM orders
		WHERE year(order_date) = 2019
	)t1
	GROUP BY  buyer_id
)t2
RIGHT JOIN users u
ON u.user_id = t2.buyer_id