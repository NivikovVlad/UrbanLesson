import sqlite3
import config


connection = sqlite3.connect('database.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL UNIQUE,
    description TEXT UNIQUE,
    price INTEGER NOT NULL UNIQUE,
    img_path TEXT UNIQUE)
    ''')


def fill_db():
    for key, value in config.price.items():
        cursor.execute(f"""
        INSERT OR IGNORE INTO Products(title, description, price, img_path) 
        VALUES('{key}', '{value[1]}', '{value[2]}', '{value[0]}')
        """)
    connection.commit()


def get_all_products():
    cursor.execute('SELECT * FROM Products')
    return cursor.fetchall()


if __name__ == '__main__':
    cursor.execute('DROP TABLE IF EXISTS Products')
    initiate_db()
    fill_db()
    test = get_all_products()
    for i in test:
        print(i)
    connection.commit()
    connection.close()