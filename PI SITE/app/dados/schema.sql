DROP TABLE IF EXISTS Pessoa;

CREATE TABLE Pessoa (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nome TEXT NOT NULL,
  senha TEXT NOT NULL,
  email TEXT NOT NULL
);
