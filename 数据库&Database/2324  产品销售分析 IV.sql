WITH a1 AS
(
	SELECT  s.product_id
	       ,user_id
	       ,SUM(quantity*price) total
	FROM sales s
	LEFT JOIN product p
	ON s.product_id = p.product_id
	GROUP BY  user_id
	         ,product_id
), a2 AS
(
	SELECT  *
	       ,rank() OVER (PARTITION BY user_id ORDER BY  total DESC) rankk
	FROM a1
)
SELECT  user_id
       ,product_id
FROM a2
WHERE rankk = 1