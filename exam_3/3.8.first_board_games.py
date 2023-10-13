SELECT
    b.name  AS name,
    b.rating,
    c.name

FROM
    board_games as b
    JOIN categories AS c
        ON b.category_id = c.id
        JOIN players_ranges as pr
            ON  pr.id = b.players_range_id
WHERE rating > 7 AND (rating > 7.50 OR LOWER(b.name) LIKE '%a%') AND pr.min_players >= 2 AND max_players <= 5

ORDER BY
    b.name ASC,
    b.rating DESC
LIMIT 5;
