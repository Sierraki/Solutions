SELECT  id
       ,'Inner' AS type
FROM tree
WHERE id NOT IN (
SELECT  id
FROM tree
WHERE id NOT IN (
SELECT  p_id AS id
FROM tree
WHERE p_id IS NOT NULL) ) AND p_id is not null
UNION
SELECT  id
       ,'Root'as type
FROM tree
WHERE p_id is null
UNION
SELECT  id
       ,'Leaf' AS type
FROM tree
WHERE id NOT IN (
SELECT  p_id
FROM tree
WHERE p_id IS NOT NULL ) AND p_id is not null 