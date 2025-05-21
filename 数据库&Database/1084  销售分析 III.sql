SELECT  product_id
       ,product_name
FROM product
WHERE product_id NOT IN ( SELECT product_id FROM sales WHERE sale_date > '2019-03-31' or sale_date < '2019-01-01' )
AND product_id IN ( SELECT product_id FROM sales )