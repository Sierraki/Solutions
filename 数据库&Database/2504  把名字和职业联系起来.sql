SELECT  person_id
       ,concat(name,'(',left(profession,1),')') name
FROM person
ORDER BY person_id desc