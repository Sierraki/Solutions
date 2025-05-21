CREATE FUNCTION getUserIDs(startDate DATE, endDate DATE, minAmount INT) RETURNS INT BEGIN RETURN (
SELECT  COUNT(distinct user_id) AS user_cnt
FROM Purchases
WHERE time_stamp BETWEEN startDate AND endDate
AND amount >= minAmount ); END