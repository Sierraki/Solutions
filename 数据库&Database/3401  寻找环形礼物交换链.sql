WITH recursive a1 AS
(
	SELECT  giver_id
	       ,receiver_id
	       ,gift_value
	       ,1 AS A
	FROM SecretSanta
	UNION ALL
	SELECT  a1.giver_id
	       ,s.receiver_id
	       ,s.gift_value
	       ,A+1
	FROM SecretSanta s
	INNER JOIN a1
	ON a1.receiver_id = s.giver_id
	WHERE A < (
	SELECT  COUNT(*)+1
	FROM SecretSanta )
) , a2 AS
(
	SELECT  distinct giver_id
	       ,receiver_id
	       ,gift_value
	FROM a1
	ORDER BY giver_id
) , a3 AS
(
	SELECT  giver_id
	       ,SUM(gift_value)over(PARTITION BY giver_id) s
	       ,COUNT(*)over(PARTITION BY giver_id) c
	FROM a2
) , a4 AS
(
	SELECT  distinct c chain_length
	       ,s total_gift_value
	FROM a3
)
SELECT  ROW_NUMBER()over(order by chain_length desc,total_gift_value DESC)chain_id
       ,chain_length
       ,total_gift_value
FROM a4
WHERE chain_length > 1