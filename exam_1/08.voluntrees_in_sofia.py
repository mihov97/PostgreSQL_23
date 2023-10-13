SELECT
    v.name as volunteers,
    v.phone_number as phone_number,
    substring(trim(REPLACE(v.address,'Sofia','')), 3)

FROM
    volunteers as v
        JOIN volunteers_departments as vd
            ON vd.id = v.department_id

WHERE vd.department_name = 'Education program assistant'
    AND
    v.address LIKE '%Sofia%'
ORDER BY
    v.name