WITH a1 AS
(
	SELECT  first_name
	       ,type
	       ,duration
	FROM calls
	LEFT JOIN contacts
	ON id = contact_id
) , a2 AS
(
	SELECT  *
	FROM a1
	WHERE type = 'incoming'
	ORDER BY duration DESC
	LIMIT 3
) , a3 AS
(
	SELECT  *
	FROM a1
	WHERE type = 'outgoing'
	ORDER BY duration DESC
	LIMIT 3
) , a4 AS
(
	SELECT  *
	FROM a2
	UNION
	SELECT  *
	FROM a3
)
SELECT  first_name
       ,type
       ,concat( lpad(floor(duration/3600),2,0),':',lpad(floor((duration-floor(duration/3600)*3600)/60),2,0),':',lpad(duration%60,2,0) )duration_formatted
FROM a4
ORDER BY type desc, duration desc, first_name desc