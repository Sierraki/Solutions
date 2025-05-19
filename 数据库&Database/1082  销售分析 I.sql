SELECT  seller_id
FROM
(
	SELECT  seller_id
	       ,rank() OVER (order by SUM(price) DESC) AS r
	FROM sales
	GROUP BY  seller_id
)t1
WHERE r = 1