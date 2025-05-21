SELECT  requester_id       AS id
       ,COUNT(accepter_id) AS num
FROM
(
	SELECT  requester_id
	       ,accepter_id
	FROM RequestAccepted
	UNION
	SELECT  accepter_id  AS requester_id
	       ,requester_id AS accepter_id
	FROM RequestAccepted
) t1
GROUP BY  requester_id
ORDER BY  COUNT(accepter_id) DESC
LIMIT 1