DROP TABLE IF EXISTS to_do;


CREATE TABLE to_do (
  Task text
  Assignee TEXT UNIQUE NOT NULL,
  Notes TEXT NOT NULL
  Status TEXT
);
