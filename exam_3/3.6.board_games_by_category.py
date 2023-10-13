SELECT
    b.id,
    b.name,
    b.release_year,
    c.name


FROM
    board_games as b
    JOIN categories as c
        ON b.category_id = c.id
WHERE c.name IN ('Wargames','Strategy Games')
ORDER BY
    release_year DESC