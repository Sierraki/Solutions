SELECT  round(AVG(order_date = customer_pref_delivery_date)*100,2) AS immediate_percentage
FROM delivery
WHERE (customer_id, order_date ) IN ( SELECT customer_id, MIN (order_date) FROM delivery GROUP BY customer_id )