SELECT  id
       ,@temp := ifnull(drink,@temp) drink
FROM CoffeeShop