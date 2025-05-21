SELECT  city
FROM listings
GROUP BY  city
HAVING AVG(price) > (
SELECT  AVG(price)
FROM Listings )
ORDER BY city