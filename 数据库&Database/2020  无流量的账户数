SELECT  COUNT(*) accounts_count
FROM streams st
WHERE year(stream_date) <> 2021
AND not exists (
SELECT  1
FROM Subscriptions Su
WHERE su.account_id = st.account_id
AND year(start_date) <> 2021
AND year(end_date) <> 2021 )