SELECT
    c.last_name,
    ROUND(CEIL(AVG(bg.rating))) AS average_rating,
    p.name AS publisher_name
FROM
    publishers as p
    JOIN board_games as bg
        ON p.id = bg.publisher_id
            JOIN creators_board_games as cbg
                ON bg.id = cbg.board_game_id
                    JOIN creators AS c
                        ON cbg.creator_id = c.id
WHERE p.name = 'Stonemaier Games'
GROUP BY
    c.last_name,
    p.name
ORDER BY average_rating DESC
;
