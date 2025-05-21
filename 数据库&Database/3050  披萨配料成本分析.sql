WITH a1 AS
(
	SELECT  t1.topping_name n1
	       ,t1.cost c1
	       ,t2.topping_name n2
	       ,t2.cost c2
	       ,t3.topping_name n3
	       ,t3.cost c3
	FROM toppings t1
	CROSS JOIN toppings t2
	CROSS JOIN toppings t3
	WHERE t1.topping_name < t2.topping_name
	AND t2.topping_name < t3.topping_name 
)
SELECT  concat_ws(',',n1,n2,n3)pizza
       ,round(c1+c2+c3,2) total_cost
FROM a1
ORDER BY total_cost desc, pizza