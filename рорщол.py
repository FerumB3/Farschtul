import  sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()
cursor.execute("""CREATE TABLE products (id INTEGER PRIMARY KEY,
       name VARCHAR NOT NULL, price FLOAT)""")
# connection.commit()
# connection.close()

connection = sqlite3.connect("database.db")
cursor = connection.cursor()
cursor.execute("""INSER INTO prodcts (name, price) VALUES
               (4.5,"apple");""")
connection.commit()
connection.close()

connection = sqlite3.connect("database.db")
cursor = connection.cursor()
cursor.execute("""SELECT * FROM PRODUCTS;""")
data = cursor.fetchall()
print(data)
connection.commit()
connection.close()