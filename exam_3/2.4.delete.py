DELETE FROM board_games
WHERE publisher_id IN
  (SELECT p.id FROM publishers AS p
    JOIN addresses AS a ON a.id = p.address_id
    WHERE SUBSTRING(town, 1, 1) = 'L'
);

DELETE FROM addresses
WHERE SUBSTRING(town, 1, 1) = 'L' ;