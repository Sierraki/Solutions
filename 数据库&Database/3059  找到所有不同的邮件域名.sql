SELECT
       substring_index (email, '@', -1) email_domain,
       COUNT(*) count
FROM
       emails
WHERE
       email LIKE '%.com'
GROUP BY
       email_domain
ORDER BY
       email_domain