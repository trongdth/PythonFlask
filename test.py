import sqlite3

connection = sqlite3.connect("data.db")

cursor = connection.cursor()
create_table = "CREATE TABLE users(id int, username text, password text)"
cursor.execute(create_table)

insert_query = "INSERT INTO users VALUES(?, ?, ?)"

users = [
    (1, 'trongdth', '123'),
    (2, 'trongdth1', '1234'),
    (3, 'trongdth2', '1235'),
]

cursor.executemany(insert_query, users)

select_row = "SELECT * FROM users"

for row in cursor.execute(select_row):
    print(row)

connection.commit()
connection.close()
