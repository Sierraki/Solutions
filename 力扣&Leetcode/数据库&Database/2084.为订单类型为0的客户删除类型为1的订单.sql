SELECT  *
FROM Orders
WHERE not (customer_id IN ( SELECT distinct customer_id FROM Orders WHERE order_type = 0 ) AND order_type = 1)