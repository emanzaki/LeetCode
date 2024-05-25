SELECT id, COUNT(id) AS num
FROM (
    SELECT requester_id AS id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id FROM RequestAccepted
) AS combined_ids
GROUP BY id
ORDER BY num desc
LIMIT 1;