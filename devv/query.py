import sqlite3

#Open database
conn = sqlite3.connect('database.db')

cur = conn.cursor()
# cur.execute('''select name from products''')

# print(cur.fetchall())

cur.execute('''INSERT INTO products (name, price, description, image, stock, categoryId) VALUES ("Quantitative aptitute", 399.00, "S.Chand", "book0.jpg", 10,  3),
("Verbal and non verbal", 231.00, "S.Chand", "book0.1.jpg", 10,  3),
("Logical reasoning", 231.00, "S.Chand", "book0.2.jpg", 10,  3),
("Suheldev", 399.00, "Amish", "book1.jpg", 10,  3),
("Sherlock holmes", 399.00, "Sir Arthur Conan Doyle", "book1.2.jpg", 10,  3),
("Treasure Island", 399.00, "Robert Louis Stevenson", "book1.3.jpg", 10,  3),
("Red white & royal blue", 399.00, "Casey McQuiston", "book2.jpg", 10,  3),
("Mary L.Trump", 231.00, "S.Chand", "book3.jpg", 10,  3)''')


cur.execute('''INSERT INTO products(name, price, description, image, stock, categoryId) VALUES ("Women", 399.00, "S.Chand", "women4.jpg", 10, 1),
("Women", 231.00, "S.Chand", "women5.jpg", 10, 1),
("Women", 231.00, "S.Chand", "women2.jpg", 10, 1),
("Tshirt", 399.00, "Amish", "tshirt1.jpg", 10, 1),
("Tshirt", 399.00, "Sir Arthur Conan Doyle", "tshirt4.jpg", 10, 1),
("Tshirt", 399.00, "Robert Louis Stevenson", "tshirt5.jpg", 10, 1),
("Kid", 399.00, "Casey McQuiston", "kid1.jpg", 10, 1),
("Kid", 231.00, "S.Chand", "kid3.jpg", 10, 1)''')


cur.execute('''INSERT INTO products(name, price, description, image, stock, categoryId) VALUES ("Dell XPS i5 10th gen", 399.00, "S.Chand", "laptop1.jpg", 10, 2),
("Apple MacBook Air Core i8 8th Gen", 231.00, "S.Chand", "laptop2.jpg", 10,  2),
("Apple MacBook Air Core i8 8th Gen", 231.00, "S.Chand", "laptop3.jpg", 10,  2),
("Apple Magic Keyboard (Wireless, Rechargable)", 3899.00, "Amish", "keyboard1.jpg", 10,  2),
("Dell Wired Keyboard - Black KB216 (580-ADMT)", 999.00, "Sir Arthur Conan Doyle", "keyboard2.jpg", 10,  2),
("Logitech MK270 Wireless Keyboard", 2599.00, "Robert Louis Stevenson", "keyboard3.jpg", 10,  2),
("Logitech G402 Optical Gaming Mouse", 3929.00, "Casey McQuiston", "mouse1.jpg", 10,  2),
("Alienware Wired/Wireless Gaming Mouse AW610M", 2310.00, "S.Chand", "mouse2.jpg", 10,  2)''')

conn.commit()

conn.close()