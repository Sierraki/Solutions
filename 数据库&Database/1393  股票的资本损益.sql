SELECT  distinct stock_name
       ,capital_gain_loss
FROM
(
	SELECT  stock_name
	       ,SUM(if(operation = 'Buy',-1*price,price)) over(PARTITION BY stock_name ) AS capital_gain_loss
	FROM Stocks
)t1