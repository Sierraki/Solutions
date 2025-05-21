SELECT  class
FROM
(
	SELECT  class
	       ,COUNT(*) AS aclass
	FROM courses
	GROUP BY  class
) AS tableA
WHERE aclass >= 5