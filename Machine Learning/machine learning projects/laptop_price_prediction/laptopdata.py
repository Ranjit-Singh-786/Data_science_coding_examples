# database.py
import sqlite3
import os

# Define the database file path
DB_FILE = os.path.join(os.path.dirname(__file__), 'data.db')

def connect_db():
    """Connect to the SQLite3 database."""
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row  # This allows accessing columns by name
    return conn

def create_table():
    """Create the laptop data table if it doesn't exist."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS laptop_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            screen_size REAL NOT NULL,
            ram INTEGER NOT NULL,
            weight REAL NOT NULL,
            processor_speed REAL NOT NULL,
            width REAL NOT NULL,
            height REAL NOT NULL,
            storage_capacity INTEGER NOT NULL,
            gpu_code INTEGER NOT NULL,
            company TEXT NOT NULL,
            type TEXT NOT NULL,
            os TEXT NOT NULL,
            generation TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_laptop_data(screen_size, ram, weight, processor_speed, width, height, storage_capacity, gpu_code, company, type_, os, generation):
    """Insert data into the laptop_data table."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO laptop_data 
        (screen_size, ram, weight, processor_speed, width, height, storage_capacity, gpu_code, company, type, os, generation)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (screen_size, ram, weight, processor_speed, width, height, storage_capacity, gpu_code, company, type_, os, generation))
    conn.commit()
    conn.close()
