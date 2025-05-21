SELECT  *
FROM genders
ORDER BY ROW_NUMBER() over(PARTITION BY gender ORDER BY user_id), length(gender) DESC