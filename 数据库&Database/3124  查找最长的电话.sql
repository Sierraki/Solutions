SELECT  first_name
       ,type
       ,concat( lpad(floor(duration/3600),2,0),':',lpad(floor((duration-floor(duration/3600)*3600)/60),2,0),':',lpad(duration%60,2,0) ) AS duration_formatted
FROM (
    SELECT  first_name
           ,type
           ,duration
    FROM calls
    LEFT JOIN contacts
    ON id = contact_id
    WHERE type = 'incoming'
    ORDER BY duration DESC
    LIMIT 3
) a2
UNION
SELECT  first_name
       ,type
       ,duration
FROM (
    SELECT  first_name
           ,type
           ,duration
    FROM calls
    LEFT JOIN contacts
    ON id = contact_id
    WHERE type = 'outgoing'
    ORDER BY duration DESC
    LIMIT 3
) a3
ORDER BY type DESC, duration DESC, first_name DESC;