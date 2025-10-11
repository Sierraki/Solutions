WITH t1 AS
(
	SELECT  e.left_operand
	       ,e.operator
	       ,e.right_operand
	       ,v.value l
	       ,e.operator O
	       ,v1.value r
	       ,v.value -v1.value A
	FROM Expressions e
	LEFT JOIN Variables v
	ON e.left_operand = v.name
	LEFT JOIN Variables v1
	ON e.right_operand = v1.name
)
SELECT  left_operand
       ,operator
       ,right_operand
       ,CASE WHEN A < 0 AND o = '<' THEN 'true'
             WHEN A > 0 AND o = '>' THEN 'true'
             WHEN A = 0 AND o = '=' THEN 'true'  ELSE 'false' END AS value
FROM t1