PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS Artist;
-- DROP TABLE IF EXISTS Superheroes;
-- DROP TABLE IF EXISTS Power;
-- DROP TABLE IF EXISTS PowerType;
-- DROP TABLE IF EXISTS SuperheroPower;
-- DROP TABLE IF EXISTS Sidekick;
-- DROP TABLE IF EXISTS Sidekicks;
-- DROP TABLE IF EXISTS Weakness;
-- DROP TABLE IF EXISTS SuperheroWeakness;

-- PRAGMA foreign_keys = ON;
-- What's up with CONSTRAINTS?
-- https://www.techonthenet.com/sqlite/foreign_keys/foreign_delete.php

CREATE TABLE `Artist` (
    `ArtistId`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `Name`    TEXT NOT NULL,
    `Gender`    TEXT NOT NULL,
);

INSERT INTO Artist VALUES (null, 'The Giphynator', 'M');