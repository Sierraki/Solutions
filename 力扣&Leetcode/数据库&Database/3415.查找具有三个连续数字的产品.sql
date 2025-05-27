SELECT  *
FROM products
WHERE name REGEXP '^[^0-9]*[0-9]{3}[^0-9]*$'; 