WITH a1 AS
(
	SELECT  *
	FROM UserActivity
	GROUP BY  username
	HAVING COUNT(*) = 1
), /*只出行一次的*/ a2 AS (
SELECT  username
FROM UserActivity
GROUP BY  username
HAVING COUNT(*) >= 2)/*出行》 = 2的名字*/
SELECT  username
       ,activity
       ,startDate
       ,endDate
FROM
(
	SELECT  *
	       ,ROW_NUMBER() OVER (PARTITION BY username ORDER BY  startDate DESC) A
	FROM UserActivity
	WHERE username IN ( SELECT * FROM a2 )
) t1
WHERE A = 2
UNION
SELECT  *
FROM a1