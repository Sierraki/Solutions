SELECT  session_id
FROM Playback
WHERE session_id NOT IN ( SELECT session_id FROM Ads, playback WHERE timestamp BETWEEN start_time AND end_time AND Playback.customer_id = Ads.customer_id)