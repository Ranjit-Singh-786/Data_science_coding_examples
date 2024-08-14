import sqlite3
from flask import g

DATABASE = 'ham_spam_predictions.db'  # Specify your separate database file name here

def get_db():
    """Connects to the specified database."""
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def close_connection(exception):
    """Closes the database connection."""
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db(app):
    """Initializes the database and creates the predictions table."""
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS predictions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email_content TEXT NOT NULL,
                result TEXT NOT NULL
            )
        ''')
        db.commit()

def insert_prediction(email_content, result):
    """Inserts a prediction into the database."""
    db = get_db()
    cursor = db.cursor()
    cursor.execute('INSERT INTO predictions (email_content, result) VALUES (?, ?)',
                   (email_content, result))
    db.commit()
