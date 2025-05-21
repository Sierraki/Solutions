WITH a1 AS
(
	SELECT  *
	FROM elements
	WHERE type = 'Metal' 
), a2 AS
(
	SELECT  *
	FROM elements
	WHERE type = 'Nonmetal' 
)
SELECT  a1.symbol metal
       ,a2.symbol nonmetal
FROM a1, a2