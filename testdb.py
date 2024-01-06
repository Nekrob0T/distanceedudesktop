from mysql.connector import connect, Error
from datetime import date
import hashlib
import os


def runDb():
    try:
        with connect(
            host="localhost",
            user="root",
            password="",
            database="pyfuture",
        ) as connection:
            # id, teacherid, title, description, author, date
            create_materials_table_query = """
            CREATE TABLE experiments (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(191),
                link VARCHAR(191)
            )
            """
            with connection.cursor() as cursor:
                cursor.execute(create_materials_table_query)
                connection.commit()
    except Error as e:
        print(e)


# string = "D:\\programing\\Projects\\Soft\\python\\forLyceum\\ssssstest.py"
# ind = string[::-1].index("\\")
# print(string)
# print(ind)
# print(string[len(string)-ind:])
# print(os.getcwd())
# s1 = "groupBox_324"
# print(s1[s1.index("_")+1:])
string = "https://aga.com"
print(string[:4])

# runDb()
