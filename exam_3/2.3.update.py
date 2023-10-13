UPDATE players_ranges CASCADE
  SET max_players = max_players + 1
  WHERE max_players = 2 AND min_players = 2;

UPDATE board_games CASCADE
  SET name = CONCAT(name, ' V2')
  WHERE release_year >= 2020;