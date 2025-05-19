SELECT  *
FROM users
WHERE email LIKE '%@%'
AND email LIKE '%.com'
ORDER BY user_id