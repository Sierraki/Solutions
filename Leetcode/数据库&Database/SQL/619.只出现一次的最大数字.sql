SELECT  t2.num
FROM
(
	SELECT  num
	FROM
	(
		SELECT  num
		       ,COUNT(num) over(PARTITION BY num)as A
		FROM mynumbers
	)t1
	WHERE A = 1
	ORDER BY num DESC
	LIMIT 1
)t2
RIGHT JOIN MyNumbers
ON MyNumbers.num = t2.num
ORDER BY num DESC
LIMIT 1