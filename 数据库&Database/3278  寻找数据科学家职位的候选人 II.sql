WITH a1 AS
(
	SELECT  distinct candidate_id
	       ,project_id
	       ,p.skill
	FROM candidates, projects p
) /*demand*/ , a2 as(
SELECT  a1.candidate_id
       ,a1.project_id
       ,a1.skill need
       ,proficiency
       ,importance
FROM a1
LEFT JOIN candidates c using
(candidate_id, skill
)
LEFT JOIN projects using
(project_id, skill
) ) , a3 AS
(
	SELECT  *
	       ,SUM(case WHEN importance < proficiency THEN 10 WHEN importance > proficiency THEN -5 else 0 end )as pos
	FROM a2
	WHERE (candidate_id, project_id) NOT IN ( SELECT candidate_id, project_id FROM a2 WHERE proficiency is null )
	GROUP BY  candidate_id
	         ,project_id
) , a4 AS
(
	SELECT  candidate_id
	       ,project_id
	       ,pos
	       ,ROW_NUMBER()over(PARTITION BY project_id ORDER BY  pos desc,candidate_id) r
	FROM a3
)
SELECT  project_id
       ,candidate_id
       ,pos+100 score
FROM a4
WHERE r = 1
ORDER BY project_id 