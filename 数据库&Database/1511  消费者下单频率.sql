WITH t1 as
(
	SELECT  o.customer_id
	FROM Orders o
	LEFT JOIN Product p
	ON o.product_id = p.product_id
	WHERE year(o.order_date) = 2020
	AND month(o.order_date) = 6
	GROUP BY  customer_id
	HAVING SUM(o.quantity*p.price) >= 100
), t2 as(
SELECT  o.customer_id
FROM Orders o
LEFT JOIN Product p
ON o.product_id = p.product_id
WHERE year(o.order_date) = 2020
AND month(o.order_date) = 7
GROUP BY  customer_id
HAVING SUM(o.quantity*p.price) >= 100)
SELECT  t2.customer_id
       ,c.name
FROM t1
LEFT JOIN t2
ON t1.customer_id = t2.customer_id
LEFT JOIN Customers c
ON t1.customer_id = c.customer_id
WHERE t2.customer_id is not null 