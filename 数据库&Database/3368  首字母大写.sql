WITH recursive a1 AS
(
	SELECT  content_id
	       ,lower(substring_index(content_text,' ',1))B
	       ,upper(left(lower(substring_index(content_text,' ',1)),1))C
	       ,substring(lower(substring_index(content_text,' ',1)),2)D
	       ,concat(upper(left(lower(substring_index(content_text,' ',1)),1)),substring(lower(substring_index(content_text,' ',1)),2))E
	       ,substring(content_text,length(substring_index(content_text,' ',1))+2)F
	       ,concat(upper(left(lower(substring_index(content_text,' ',1)),1)),substring(lower(substring_index(content_text,' ',1)),2)) AS G
	FROM user_content
	UNION ALL
	SELECT  content_id
	       ,lower(substring_index(F,' ',1))B
	       ,upper(left(lower(substring_index(F,' ',1)),1))C
	       ,substring(lower(substring_index(F,' ',1)),2)D
	       ,concat(upper(left(lower(substring_index(F,' ',1)),1)),substring(lower(substring_index(F,' ',1)),2))E
	       ,substring(F,length(substring_index(F,' ',1))+2)F
	       ,concat(G,' ',E) G
	FROM a1
	WHERE length(B) > 0 
) , a2 AS
(
	SELECT  content_id
	       ,G
	       ,ROW_NUMBER()over(PARTITION BY content_id ORDER BY  length(G) DESC) r
	FROM a1
)
SELECT  a2.content_id
       ,content_text original_text
       ,substring(G,locate(' ',G)+1) converted_text
FROM a2
LEFT JOIN user_content u
ON u.content_id = a2.content_id
WHERE r = 1 