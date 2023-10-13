SELECT
    o.name AS owner,
    count(owner_id) AS count_of_animals
FROM
    animals AS a
        join owners as o
            on o.id = a.owner_id
GROUP BY o.name
ORDER BY
    count(owner_id) DESC,
    o.name ASC
LIMIT 5
;