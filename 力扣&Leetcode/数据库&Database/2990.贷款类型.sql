WITH a1 AS
(
	SELECT  user_id
	FROM loans
	WHERE loan_type = 'Refinance' 
), a2 AS
(
	SELECT  user_id
	FROM loans
	WHERE loan_type = 'Mortgage' 
)
SELECT  distinct a1.user_id
FROM a1
LEFT JOIN a2
ON a1.user_id = a2.user_id
WHERE a2.user_id is not null
ORDER BY a1.user_id 