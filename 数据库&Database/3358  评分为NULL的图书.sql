SELECT  book_id
       ,title
       ,author
       ,published_year
FROM books
WHERE rating is null
ORDER BY book_id