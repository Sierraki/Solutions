SELECT  round(SUM(item_count*order_occurrences)/ SUM(order_occurrences),2) average_items_per_order
FROM orders