WITH a1 AS
(
	SELECT  customer_id
	       ,product_id
	       ,COUNT(*) OVER (PARTITION BY customer_id,product_id) A
	FROM orders
), a2 AS
(
	SELECT  *
	       ,rank() OVER (PARTITION BY customer_id ORDER BY  A DESC ) B
	FROM a1
)
SELECT  distinct a2.customer_id
       ,a2.product_id
       ,p.product_name
FROM a2
JOIN Products p
ON p.product_id = a2.product_id
WHERE B = 1