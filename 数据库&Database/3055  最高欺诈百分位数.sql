WITH a1 AS
(
	SELECT  *
	       ,round(percent_rank()over(PARTITION BY state ORDER BY  fraud_score DESC),2) r
	FROM fraud
)
SELECT  *
FROM a1