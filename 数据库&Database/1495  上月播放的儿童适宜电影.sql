WITH a1 AS
(
	SELECT  content_id
	FROM TVProgram
	WHERE year(program_date ) = 2020
	AND month(program_date ) = 6 
), a2 AS
(
	SELECT  content_id
	       ,title
	FROM Content
	WHERE Kids_content = 'Y'
	AND content_type = 'Movies' 
)
SELECT  distinct title
FROM
(
	SELECT  a1.content_id
	       ,title
	FROM a1
	LEFT JOIN a2
	ON a1.content_id = a2.content_id
	WHERE title is not null
)t3