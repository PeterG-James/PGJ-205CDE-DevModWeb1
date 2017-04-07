DROP TABLE IF EXISTS comments_table;


CREATE TABLE comments_table (
    id integer PRIMARY KEY,
    name text NOT NULL,
    comments text NOT NULL
    );