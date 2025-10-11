SELECT  ifnull(round(fz/fm,2),0) AS accept_rate
FROM
(
	SELECT  COUNT(*) AS fz
	       ,'a'as id
	FROM
	(
		SELECT  distinct requester_id
		       ,accepter_id
		FROM RequestAccepted
	)t1
)t2, (
SELECT  COUNT(*) AS fm
       ,'a'as id
FROM
(
	SELECT  distinct sender_id
	       ,send_to_id
	FROM FriendRequest
)t4)t3
WHERE t2.id = t3.id