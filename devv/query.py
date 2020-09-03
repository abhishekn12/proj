import sqlite3

#Open database
conn = sqlite3.connect('database.db')

cur = conn.cursor()

cur.execute('''INSERT INTO products (name, price, description, image, stock, categoryId) VALUES ("Quantitative aptitute", 399.00, "S.Chand", "book0.jpg", 10, 1)''')

conn.commit()

conn.close()