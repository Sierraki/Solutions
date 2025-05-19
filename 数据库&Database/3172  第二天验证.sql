SELECT  e.user_id
FROM emails e
LEFT JOIN texts t
ON e.email_id = t.email_id
WHERE datediff (date (action_date), date (signup_date)) = 1
AND signup_action = "Verified"
ORDER BY e.user_id