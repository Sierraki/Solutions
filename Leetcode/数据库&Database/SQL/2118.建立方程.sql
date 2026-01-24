WITH a1 AS
(
	SELECT  power p
	       ,if(factor > 0,concat('+',factor),factor) f
	FROM terms
), a2 AS
(
	SELECT  *
	       ,CASE WHEN p = 0 THEN f
	             WHEN p = 1 THEN concat(f,'X')
	             WHEN p > 1 THEN concat(f,'X','^',p) END AS A
	FROM a1
)
SELECT  concat(group_concat(A ORDER BY  p DESC separator''),'=0') equation
FROM a2