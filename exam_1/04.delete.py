DELETE FROM
    volunteers_departments
WHERE
    id = (SELECT id from volunteers_departments
WHERE department_name = 'Education program assistant')
;