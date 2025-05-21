WITH a1 AS
(
	SELECT  account_id
	       ,amount
	       ,date_format(day,'%Y-%m')m
	FROM Transactions
	WHERE type = 'creditor'
	ORDER BY account_id, day
), a2 AS
(
	SELECT  distinct a1.account_id id
	       ,m
	       ,max_income-SUM(amount) OVER (PARTITION BY a1.account_id,m) A
	FROM a1
	LEFT JOIN Accounts ac
	ON ac.account_id = a1.account_id
), a3 AS
(
	SELECT  id
	       ,concat(m,'-01')m
	       ,A
	       ,lead(m) OVER (PARTITION BY id ORDER BY  m ASC)B
	FROM a2
	WHERE A < 0
), a4 AS
(
	SELECT  id
	       ,m
	       ,A
	       ,concat(B,'-01') B
	FROM a3
), a5 AS
(
	SELECT  id
	       ,m
	       ,A
	       ,B
	       ,timestampdiff(month,m,B) C
	FROM a4
	WHERE B is not null
)
SELECT  distinct id account_id
FROM a5
WHERE C = 1 