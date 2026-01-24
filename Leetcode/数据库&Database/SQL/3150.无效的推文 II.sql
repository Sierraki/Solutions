SELECT  tweet_id
FROM tweets
WHERE content regexp '@.*@.*@.*@' or length(content) > 140 or content regexp '#.*#.*#.*#'
ORDER BY tweet_id