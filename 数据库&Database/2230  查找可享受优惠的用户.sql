CREATE PROCEDURE getUserIDs(startDate DATE, endDate DATE, minAmount INT) BEGIN # Write your MySQL query statement below.
SELECT  distinct user_id
FROM purchases
WHERE amount >= minamount
AND time_stamp BETWEEN startdate AND enddate
ORDER BY user_id; END