WITH recursive a1 AS
(
	SELECT  tweet_id
	       ,substring(tweet,locate('#',tweet)) B
	       ,/*第一个#后面的句子*/ substring_index(substring(tweet,locate('#',tweet)),' ',1) C
	       ,/*提取关键字*/ 0 AS D
	FROM tweets
	UNION ALL
	SELECT  tweet_id
	       ,substring(substring(B,2),locate('#',substring(B,2))) B
	       ,/*第一个#后面的句子*/ substring_index(substring(B,locate('#',B)),' ',1) C
	       ,D+1
	FROM a1
	WHERE locate('#', B) > 0 
)
SELECT  C hashtag
       ,COUNT(*) count
FROM a1
WHERE D <> 0
GROUP BY  c
ORDER BY  count desc
         ,hashtag DESC
LIMIT 3