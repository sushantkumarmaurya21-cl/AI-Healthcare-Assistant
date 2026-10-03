import sqlite3


def create_database():
    conn = sqlite3.connect('healthcare.db')

    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_name TEXT,
            disease TEXT
        )
    ''')

    conn.commit()
    conn.close()


create_database()