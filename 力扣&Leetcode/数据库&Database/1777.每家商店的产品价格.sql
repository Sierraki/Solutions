SELECT  product_id
       ,SUM(if(store = 'store1',price,null)) store1
       ,SUM(if(store = 'store2',price,null)) store2
       ,SUM(if(store = 'store3',price,null)) store3
FROM Products
GROUP BY  1