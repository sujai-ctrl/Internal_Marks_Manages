import sqlite3

DB_NAME = "database/internal_marks.db"


def connect_db():
    return sqlite3.connect(DB_NAME)


def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            register_no TEXT UNIQUE,
            name TEXT,
            department TEXT,
            semester TEXT,
            test1 REAL,
            test2 REAL,
            assignment REAL,
            attendance REAL,
            internal_mark REAL
        )
    """)

    conn.commit()
    conn.close()


def add_student(data):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO students
        (register_no, name, department, semester,
         test1, test2, assignment, attendance, internal_mark)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, data)

    conn.commit()
    conn.close()


def get_students():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    conn.close()
    return records