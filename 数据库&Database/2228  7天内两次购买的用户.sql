WITH a1 AS
(
	SELECT  purchase_id
	       ,user_id
	       ,purchase_date d1
	       ,lag(purchase_date) OVER (PARTITION BY user_id ORDER BY  purchase_date ) d2
	FROM purchases
), a2 AS
(
	SELECT  *
	       ,timestampdiff(day,d2,d1) diff
	FROM a1
	WHERE d2 is not null
)
SELECT  distinct user_id
FROM a2
WHERE diff <= 7
ORDER BY user_id