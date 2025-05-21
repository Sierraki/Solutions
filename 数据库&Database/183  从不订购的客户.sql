SELECT  name AS Customers
FROM Customers
LEFT JOIN orders
ON Customers.id = Orders.customerId
WHERE customerId is null