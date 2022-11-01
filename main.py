import sqlite3
from sqlite3 import Error

def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except Error as e:
        print(e)

    return conn

def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error as e:
        print(e)
# def create_student(conn, student):
#     try:
#         sql = '''INSERT INTO students
#         (fullname, mark, hobby, birthday_date, is_married)
#         VALUES (?,?,?,?,?)'''
#         cursor = conn.cursor()
#         cursor.execute(sql, student)
#         conn.commit()
#     except Error as e:
#         print(e)

def delet_student(conn, student):
    try:
        sql = '''DELETE FROM students WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (id, ))
        conn.commit()
    except Error as e:
        print(e)

def update_student_mark_and_marital_status(conn, student):
    try:
        sql = '''UPDATE students SET mark = ?, is_married = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, student)
        conn.commit()
    except Error as e:
        print(e)

def select_all_student(conn):
    try:
        sql = '''SELECT * FROM students'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchmany(3)
        for row in rows:
            print(row)
    except Error as e:
        print(e)

connection = create_connection("""gr_21_2.db""")
create_students_table = '''
CREATE TABLE students(
id INTEGER PRIMARY KEY AUTOINCREMENT, 
fullname VARCHAR (200) NOT NULL ,
mark DOUBLE (5, 2) NOT NULL DEFAULT 0.0,
hobby TEXT DEFAULT NULL,
birthday_date DATE NOT NULL,
is_married BOOLEAN DEFAULT FALSE
)
'''

if connection is not None:
    print('Connected succesfully!')
    select_all_student(connection)
    create_table(connection, create_students_table)
    # create_student(connection, ('esen mambetov', 20.56, 'chess', '2003-11-09', False))
    update_student_mark_and_marital_status(connection, (15.08, False, 1))
    print('Done!')
