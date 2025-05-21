SELECT  *
FROM products
WHERE description regexp 'SN\\d{4}-\\d{4}$'
UNION
SELECT  *
FROM products
WHERE description regexp 'SN\\d{4}-\\d{4}[ ]'
ORDER BY product_id 