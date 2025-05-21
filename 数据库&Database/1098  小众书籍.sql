WITH a1 AS
(
	SELECT  o.book_id
	       ,b.name
	       ,o.quantity
	       ,o.dispatch_date
	       ,b.available_from
	FROM orders o
	LEFT JOIN Books b
	ON o.book_id = b.book_id
	WHERE o.dispatch_date BETWEEN '2018-06-23' AND '2019-06-23'
	AND b.available_from < '2019-05-23'
), a2 AS
(
	SELECT  book_id
	FROM a1
	GROUP BY  book_id
	HAVING SUM(quantity) >= 10
), a3 AS
(
	SELECT  book_id
	FROM Books
	WHERE available_from < '2019-05-23'
), a4 AS
(
	SELECT  *
	FROM a3 except
	SELECT  *
	FROM a2
)
SELECT  a4.book_id
       ,b1.name
FROM a4
LEFT JOIN books b1
ON b1.book_id = a4.book_id