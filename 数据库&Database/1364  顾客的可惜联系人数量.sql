WITH a1 AS
(
	SELECT  customer_name
	       ,COUNT(*) A
	FROM contacts co
	LEFT JOIN customers cu
	ON co.user_id = cu.customer_id
	GROUP BY  customer_name
), /*Customers的联系人数量*/ a2 AS (
SELECT  customer_name
       ,COUNT(*) B
FROM contacts co
LEFT JOIN customers cu
ON co.user_id = cu.customer_id
WHERE contact_name IN ( SELECT customer_name FROM Customers )
GROUP BY  customer_name)/*Customers的可信人数量*/
SELECT  i.invoice_id
       ,c.customer_name
       ,price
       ,ifnull(A,0) contacts_cnt
       ,ifnull(B,0) trusted_contacts_cnt
FROM Invoices i
LEFT JOIN Customers c
ON i.user_id = c.customer_id
LEFT JOIN a1
ON c.customer_name = a1.customer_name
LEFT JOIN a2
ON c.customer_name = a2.customer_name
ORDER BY invoice_id