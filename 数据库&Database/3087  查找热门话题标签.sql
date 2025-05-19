WITH a1 AS
(
	SELECT  concat('#',substring_index(substring_index(tweet,'#',-1),' ',1)) B
	FROM tweets
	WHERE year(tweet_date) = 2024
	AND month(tweet_date) = 2 
) , a2 AS
(
	SELECT  B
	       ,COUNT(*)A
	FROM a1
	GROUP BY  B
) , a3 AS
(
	SELECT  *
	       ,ROW_NUMBER()over(order by A desc,B DESC)r
	FROM a2
)
SELECT  B HASHTAG
       ,A HASHTAG_COUNT
FROM a3
WHERE r <= 3
ORDER BY a desc, b DESC 