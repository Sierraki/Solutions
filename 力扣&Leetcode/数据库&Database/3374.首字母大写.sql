WITH RECURSIVE cte
(n, content_id, converted_text
) AS (
SELECT  0 n
       ,content_id
       ,lower(content_text) converted_text
FROM user_content
UNION ALL
SELECT  n + 1 n
       ,content_id
       ,regexp_replace(converted_text,concat('\\b',CHAR(n + 97 USING utf8)),CHAR(n + 65 USING utf8)) converted_text
FROM cte
WHERE n < 26 )
SELECT  content_id
       ,content_text original_text
       ,converted_text
FROM user_content
JOIN cte USING
(content_id
)
WHERE n = 26