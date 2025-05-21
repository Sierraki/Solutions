SELECT  distinct t.id
       ,name
FROM
(
	SELECT  *
	       ,LEAD(login_date,4)OVER(PARTITION BY id ORDER BY  login_date) AS next_day
	FROM
	(
		SELECT  *
		FROM Logins
		GROUP BY  1
		         ,2
	) tmp
) t
JOIN Accounts a
ON a.id = t.id
WHERE DATEDIFF(next_day, login_date) = 4
ORDER BY id