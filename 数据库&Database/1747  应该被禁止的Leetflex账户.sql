SELECT  DISTINCT l1.account_id
FROM loginfo l1
LEFT JOIN loginfo l2
ON l1.account_id = l2.account_id AND l1.ip_address <> l2.ip_address
WHERE (l2.login >= l1.login AND l2.login <= l1.logout) OR (l2.logout >= l1.login AND l2.logout <= l1.logout); 