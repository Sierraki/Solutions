SELECT  date_format(trans_date,'%Y-%m')          AS month
       ,country
       ,COUNT(state)as trans_count
       ,COUNT( if( state = 'approved',1,null ) ) AS approved_count
       ,SUM(amount)as trans_total_amount
       ,SUM( if( state = 'approved',amount,0 ) ) AS approved_total_amount
FROM transactions
GROUP BY  month
         ,country