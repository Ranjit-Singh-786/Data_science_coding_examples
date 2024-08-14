import sqlite3

def connect_db():
    conn = sqlite3.connect('farmer_guider/form_data.db')  # Path to your SQLite database
    return conn

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS form_data (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        n REAL,
                        p REAL,
                        k REAL,
                        temperature REAL,
                        humidity REAL,
                        ph REAL,
                        rainfall REAL
                    )''')
    conn.commit()
    conn.close()

def insert_form_data(n, p, k, temperature, humidity, ph, rainfall):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO form_data (n, p, k, temperature, humidity, ph, rainfall)
                      VALUES (?, ?, ?, ?, ?, ?, ?)''',
                   (n, p, k, temperature, humidity, ph, rainfall))
    conn.commit()
    conn.close()
