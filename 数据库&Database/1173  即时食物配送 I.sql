SELECT  round(AVG( CASE WHEN order_date = customer_pref_delivery_date THEN 1 else 0 end)*100,2) immediate_percentage
FROM delivery