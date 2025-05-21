SELECT  s.product_id
       ,s.year first_year
       ,s.quantity
       ,s.price
FROM Sales s,
(
	SELECT  product_id
	       ,MIN(year) year
	FROM Sales
	GROUP BY  product_id
) a
WHERE s.product_id = a.product_id
AND s.year = a.year