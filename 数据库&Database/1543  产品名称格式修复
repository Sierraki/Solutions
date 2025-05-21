WITH a1 AS
(
	SELECT  sale_id
	       ,trim(lower(product_name))product_name
	       ,date_format(sale_date,'%Y-%m')sale_date
	FROM sales
)
SELECT  distinct product_name
       ,sale_date
       ,COUNT(*) OVER (PARTITION BY product_name,sale_date ) total
FROM a1
ORDER BY product_name, sale_date