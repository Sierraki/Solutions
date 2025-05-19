WITH a1 AS
(
	SELECT  s.product_id
	       ,user_id
	       ,SUM(quantity*price) total
	FROM sales s
	LEFT JOIN product p
	ON s.product_id = p.product_id
	GROUP BY  user_id
)
SELECT  user_id
       ,total spending
FROM a1
ORDER BY spending desc