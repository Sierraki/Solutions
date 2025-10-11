select
    book_id,
    title,
    author,
    genre,
    publication_year,
    total_copies current_borrowers
from
    borrowing_records
    left join library_books using (book_id)
where
    return_date is null
group by
    book_id
having
    count(*) = total_copies
order by
    current_borrowers desc,
    title