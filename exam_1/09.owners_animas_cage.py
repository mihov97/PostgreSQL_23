SELECT
    concat(o.name, ' - ',a.name) AS "Owners - Animals",
    o.phone_number AS "Phone Number",
    ac.cage_id AS "Cage ID"
FROM
    owners as o
        JOIN animals as a
            ON o.id = a.owner_id
                JOIN animals_cages as ac
                    ON ac.animal_id = a.id
                        Join animal_types AS at
                            on at.id = a.animal_type_id
WHERE at.animal_type = 'Mammals'
ORDER BY
    o.name ASC,
    a.name DESC
;