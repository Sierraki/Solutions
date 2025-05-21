SELECT  sp.salesperson_id
       ,name
       ,SUM(ifnull(price,0) )total
FROM salesperson sp
LEFT JOIN Customer c
ON sp.salesperson_id = c.salesperson_id
LEFT JOIN sales sa
ON sa.Customer_id = c.Customer_id
GROUP BY  sp.salesperson_id