CREATE OR REPLACE FUNCTION fn_creator_with_board_games(ime VARCHAR(30))
    RETURNS INT AS
$$
    DECLARE final_res INT;
    BEGIN
        SELECT
            COUNT(*)
        FROM
            board_games as bg
        JOIN creators_board_games AS cbg
            ON cbg.board_game_id = bg.id
        JOIN creators as c
            ON cbg.creator_id = c.id
        WHERE c.first_name = ime
        INTO final_res;

        RETURN final_res;

    END;
$$
LANGUAGE plpgsql;


SELECT fn_creator_with_board_games('Bruno')