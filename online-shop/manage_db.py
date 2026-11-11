import sqlite3
from ShopORM import Session
con = sqlite3.connect('shop.db')
con.execute("PRAGMA foreign_keys = ON;")
cur = con.cursor()

# cur.execute("""CREATE TABLE items(id INTEGER PRIMARY KEY AUTOINCREMENT, article TEXT, type TEXT, manufacturer TEXT, amount INTEGER, price DECIMAL, description TEXT)""")



# # 1. Добавление одной записи
# cur.execute('''
#     INSERT INTO items (article, type, manufacturer, amount, price, description)
#     VALUES (?, ?, ?, ?, ?, ?)
# ''', ('A101', 'Смартфон', 'Apple', 10, 999.99, 'iPhone 15 Pro'))
#
# # 2. Массовое добавление нескольких записей (рекомендуемый способ)
# many_items = [
#     ('A102', 'Смартфон', 'Samsung', 15, 849.50, 'Galaxy S24'),
#     ('B201', 'Ноутбук', 'Asus', 5, 1200.00, 'ZenBook 14'),
#     ('C305', 'Наушники', 'Sony', 25, 299.99, 'WH-1000XM5')
# ]
#
# cur.executemany('''
#     INSERT INTO items (article, type, manufacturer, amount, price, description)
#     VALUES (?, ?, ?, ?, ?, ?)
# ''', many_items)
#
# # Проверка результата
# cur.execute("SELECT * FROM items")
# print(cur.fetchall())


# cur.execute("""CREATE TABLE """)
# cur.execute("""CREATE TABLE """)
# cur.execute("""CREATE TABLE """)
# cursor.execute(
#     '''CREATE TABLE users (id SMALLSERIAL PRIMARY KEY NOT NULL, email VARCHAR(100) NOT NULL,
#      username VARCHAR(50) NOT NULL, password VARCHAR(100) NOT NULL)''')

# cur.execute('ALTER TABLE users ADD COLUMN role TEXT NOT NULL DEFAULT user')


con.commit()
con.close()