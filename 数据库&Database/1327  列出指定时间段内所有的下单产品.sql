SELECT  p.product_name
       ,t.unit
FROM
(
	SELECT  product_id
	       ,SUM(unit) AS unit
	FROM orders
	WHERE year(order_date) = 2020
	AND month(order_date) = 2
	GROUP BY  product_id
	HAVING unit >= 100
) AS t, products AS p
WHERE p.product_id = t.product_id 