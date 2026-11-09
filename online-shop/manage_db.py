import sqlite3
from ShopORM import Session
con = sqlite3.connect('shop.db')
con.execute("PRAGMA foreign_keys = ON;")
cur = con.cursor()


con.commit()
con.close()