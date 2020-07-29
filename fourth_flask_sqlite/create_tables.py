import sqlite3

connecton = sqlite3.connect('data.db')
cursor = connecton.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (name text, price real)"
cursor.execute(create_table)

# cursor.execute("INSERT INTO items VALUES ('test', 1.99)")

connecton.commit()
connecton.close()
