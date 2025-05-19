SELECT  distinct artist
       ,COUNT(*) over(PARTITION BY artist) occurrences
FROM spotify
ORDER BY occurrences desc, artist