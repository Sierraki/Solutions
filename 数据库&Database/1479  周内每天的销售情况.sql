# Write your MySQL query statement below
SELECT  distinct b.item_category AS Category
       ,ifnull(SUM(case WHEN dayofweek(a.order_date) = 2 THEN a.quantity end),0) Monday
       ,ifnull(SUM(case WHEN dayofweek(a.order_date) = 3 THEN a.quantity end),0) Tuesday
       ,ifnull(SUM(case WHEN dayofweek(a.order_date) = 4 THEN a.quantity end),0) Wednesday
       ,ifnull(SUM(case WHEN dayofweek(a.order_date) = 5 THEN a.quantity end),0) Thursday
       ,ifnull(SUM(case WHEN dayofweek(a.order_date) = 6 THEN a.quantity end),0) Friday
       ,ifnull(SUM(case WHEN dayofweek(a.order_date) = 7 THEN a.quantity end),0) Saturday
       ,ifnull(SUM(case WHEN dayofweek(a.order_date) = 1 THEN a.quantity end),0) Sunday
FROM Orders a
RIGHT JOIN Items b
ON a.item_id = b.item_id
GROUP BY  Category
ORDER BY  Category