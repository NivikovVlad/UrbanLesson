"""
Выбор элементов и функции в SQL запросах
Цель: научится использовать функции внутри запросов языка SQL и использовать их в решении задачи
"""

import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL)
''')


def fill_database():
    """
    Заполняем таблицу
    """
    for i in range(1, 11):
        cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)",
                       (f"User{i}", f"example{i}@gmail.com", f"{i * 10}", f"{1000}"))


def new_balance():
    """
    Изменить баланс
    """
    cursor.execute('SELECT COUNT(*) FROM Users')
    row_count = cursor.fetchone()
    for i in range(1, row_count[0]+1):
        if i % 2 != 0:
            cursor.execute('UPDATE Users SET balance = ? WHERE id = ?', (500, i))


def del_row():
    """
    Удалить строки
    """
    cursor.execute('SELECT COUNT(*) FROM Users')
    row_count = cursor.fetchone()
    for i in range(1, row_count[0]+1, 3):
        cursor.execute('DELETE FROM Users WHERE id = ?', (i,))


def viborka():
    """
    Имя: <username> | Почта: <email> | Возраст: <age> | Баланс: <balance>
    """
    cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != ?', (60,))
    result = cursor.fetchall()
    for user in result:
        print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')


if __name__ == '__main__':
    # fill_database()
    # new_balance()
    # del_row()
    # viborka()

    cursor.execute('DELETE FROM Users WHERE id = ? ', (6,))
    cursor.execute('SELECT COUNT(*) FROM Users')
    total_users = cursor.fetchone()[0]
    cursor.execute('SELECT SUM(balance) FROM Users')
    all_balances = cursor.fetchone()[0]
    print(all_balances / total_users)
    cursor.execute('SELECT AVG(balance) FROM Users')
    all_balances1 = cursor.fetchone()[0]
    print(all_balances1)



    # cursor.execute('DROP TABLE IF EXISTS Users')
    connection.commit()
    connection.close()
