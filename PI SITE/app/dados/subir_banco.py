# ARQUIVO USADO PARA ADMINISTRAR MANUALMENTE UMA BASE DE DADOS

import sqlite3

connection = sqlite3.connect('dados/4thenature.db')

connection.execute("PRAGMA foreign_keys = ON")

with open('dados/schema.sql') as f:
    connection.executescript(f.read())

connection.commit()
connection.close()