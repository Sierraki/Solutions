WITH a1 AS
(
	SELECT  name customer_name
	       ,o.customer_id
	       ,order_id
	       ,order_date
	FROM Orders o
	JOIN Customers c
	ON o.customer_id = c.customer_id
), a2 AS
(
	SELECT  *
	       ,ROW_NUMBER() OVER (PARTITION BY customer_name ,customer_id ORDER BY  order_date DESC) A
	FROM a1
)
SELECT  customer_name
       ,customer_id
       ,order_id
       ,order_date
FROM a2
WHERE A <= 3
ORDER BY customer_name asc, customer_id ASC , order_date desc