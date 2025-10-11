with
       a1 as (
              select distinct
                     p1.category c1,
                     p2.category c2
              from
                     productinfo p1,
                     productinfo p2
              where
                     p1.category < p2.category
       ),
       a2 as (
              select
                     user_id,
                     product_id,
                     category
              from
                     productpurchases
                     left join productinfo using (product_id)
       ),
       a3 as (
              select distinct
                     c1,
                     c2,
                     a2.user_id u1,
                     a22.user_id u2
              from
                     a1
                     left join a2 on a1.c1 = a2.category
                     left join a2 a22 on a1.c2 = a22.category
              where
                     a2.user_id = a22.user_id
              order by
                     c1,
                     c2
       )
select
       c1 category1,
       c2 category2,
       count(*) customer_count
from
       a3
group by
       c1,
       c2
having
       customer_count >= 3
order by
       customer_count desc,
       c1,
       c2