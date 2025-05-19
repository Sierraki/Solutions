WITH aa as
(
	SELECT  id
	       ,country
	       ,SUM(points)'points'
	       ,winery
	FROM Wineries
	GROUP BY  country
	         ,winery
), a1 as(
SELECT  *
       ,rank() OVER (PARTITION BY country ORDER BY  points desc,winery) rankk
FROM aa), /*排名*/ a2 AS (
SELECT  distinct country
FROM wineries ), a3 AS
(
	SELECT  a2.country
	       ,concat(winery,' (',points,')')top_winery
	FROM a2
	LEFT JOIN a1
	ON a2.country = a1.country
	WHERE rankk = 1
), /*第一名*/ a4 AS (
SELECT  country
       ,concat(winery,' (',points,')')second_winery
FROM a1
WHERE rankk = 2), /*2*/ a5 AS (
SELECT  country
       ,concat(winery,' (',points,')')third_winery
FROM a1
WHERE rankk = 3) /*3*/
SELECT  a3.country
       ,top_winery
       ,ifnull(second_winery,'No second winery')second_winery
       ,ifnull(third_winery,'No third winery')third_winery
FROM a3
LEFT JOIN a4
ON a3.country = a4.country
LEFT JOIN a5
ON a3.country = a5.country
ORDER BY a3.country