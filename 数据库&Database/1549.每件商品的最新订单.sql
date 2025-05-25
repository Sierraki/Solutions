WITH a1 AS
(
	SELECT  product_id
	       ,customer_id
	       ,order_id
	       ,order_date
	       ,rank() OVER (PARTITION BY product_id ORDER BY  order_date DESC) AA
	FROM orders
)
SELECT  p.product_name
       ,a1.product_id
       ,order_id
       ,order_date
FROM a1
JOIN Products p
ON a1.product_id = p.product_id
WHERE AA = 1
ORDER BY p.product_name asc, a1.product_id asc, order_id asc