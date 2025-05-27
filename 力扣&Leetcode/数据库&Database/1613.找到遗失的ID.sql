WITH recursive a1 AS
(
	SELECT  1 AS id
	UNION
	SELECT  id + 1
	FROM a1
	WHERE id <= (
	SELECT  MAX(customer_id)-1
	FROM Customers )
)
SELECT  id ids
FROM a1
LEFT JOIN customers c
ON c.customer_id = a1.id
WHERE customer_id is null
ORDER BY id asc