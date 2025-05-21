SELECT  buyer_id
FROM
(
	SELECT  buyer_id
	       ,product_name
	FROM sales s
	LEFT JOIN Product p
	ON s.product_id = p.product_id
	WHERE product_name = 'iphone' OR product_name = 's8' 
) t1
GROUP BY  buyer_id
HAVING SUM(CASE WHEN product_name = 's8' THEN 1 ELSE 0 END) > 0 AND SUM(CASE WHEN product_name = 'iphone' THEN 1 ELSE 0 END) = 0;