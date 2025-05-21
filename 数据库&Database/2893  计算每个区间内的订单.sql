SELECT  FLOOR((minute-1)/6)+1 interval_no
       ,SUM(order_count) total_orders
FROM orders
GROUP BY  FLOOR((minute-1)/6)+1
ORDER BY  interval_no