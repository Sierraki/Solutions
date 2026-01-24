WITH a1 AS
(
	SELECT  user_id
	       ,spend_date
	       ,platform
	       ,amount
	       ,COUNT(*) OVER (PARTITION BY spend_date,user_id ) A
	FROM spending
), a2 AS
(
	SELECT  *
	FROM a1
	WHERE A = 1
), a3 AS
(
	SELECT  *
	FROM a1
	WHERE A = 2
), a4 AS
(
	SELECT  spend_date
	       ,platform
	       ,SUM(amount) OVER (PARTITION BY spend_date,platform) total_amount
	       ,COUNT(*) OVER (PARTITION BY spend_date,platform) total_users
	FROM a2
), a5 AS
(
	SELECT  distinct spend_date
	       ,'both' AS platform
	       ,SUM(amount) OVER (PARTITION BY spend_date,user_id) total_amount
	       ,COUNT(*) OVER (PARTITION BY spend_date,user_id)-1 total_users
	FROM a3
), a6 AS
(
	SELECT  *
	FROM a4
	UNION ALL
	SELECT  *
	FROM a5
), a7 AS
(
	SELECT  'desktop' AS platform
	UNION
	SELECT  'mobile' AS platform
	UNION
	SELECT  'both' AS platform
), a8 AS
(
	SELECT  distinct spend_date
	       ,a7.platform
	FROM spending
	CROSS JOIN a7
)
SELECT  distinct a8.spend_date
       ,a8.platform
       ,ifnull(a6.total_amount,0) total_amount
       ,ifnull(a6.total_users,0) total_users
FROM a6
RIGHT JOIN a8
ON a6.spend_date = a8.spend_date AND a6.platform = a8.platform