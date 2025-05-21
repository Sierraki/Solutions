SELECT  email AS Email
FROM
(
	SELECT  email
	       ,COUNT(*) AS a1
	FROM person
	GROUP BY  email
) AS a2
WHERE a1 <> 0
AND a1 <> 1