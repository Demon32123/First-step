import sqlite3

# Подключение базы данных
conn = sqlite3.connect('Productinfo.db')
cur = conn.cursor()

# Создание таблицы
cur.execute("""CREATE TABLE IF NOT EXISTS PRODUCTINFO(
    Price REAL,
    Name TEXT,
    ID INTEGER);
""")
conn.commit()


# Добавление в базу 2 предметов
for kol in range(0, 2):
    Price = float(input("Цена: "))
    Name = input("Нaзвание: ")
    ID = int(input('ID: '))
    PRD = (Price, Name, ID)
    cur.execute("""INSERT INTO PRODUCTINFO VALUES(?, ?, ?);""", PRD)
    conn.commit()


# # Просмотр базы
# cur.execute("SELECT * FROM PRODUCTINFO;")
# result = cur.fetchall()
# print(result)
