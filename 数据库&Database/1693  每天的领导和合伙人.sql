SELECT  date_id
       ,make_name
       ,COUNT(distinct lead_id)     AS unique_leads
       ,COUNT(distinct partner_id ) AS unique_partners
FROM dailysales
GROUP BY  date_id
         ,make_name