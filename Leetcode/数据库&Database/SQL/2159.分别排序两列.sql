WITH a1 AS
(
	SELECT  first_col
	       ,ROW_NUMBER() OVER (order by first_col) A
	FROM data
	ORDER BY first_col
), a2 AS
(
	SELECT  second_col
	       ,ROW_NUMBER() OVER (order by second_col DESC) A
	FROM data
	ORDER BY second_col DESC
)
SELECT  first_col
       ,second_col
FROM a1
LEFT JOIN a2
ON a1.A = a2.A
ORDER BY first_col, second_col desc