CREATE TEMPORARY TABLE temp_table AS
SELECT  customer_id
       ,year(order_date) d
       ,SUM(price)total
FROM orders
GROUP BY  customer_id
         ,d
ORDER BY  d
SELECT  *

FROM temp_table DROP TEMPORARY TABLE temp_table