import sqlite3

def init_db():
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            price TEXT,
            rating TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_books(books):
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    for book in books:
        cursor.execute('''
            INSERT INTO books (title, price, rating)
            VALUES (?, ?, ?)
        ''', (book['title'], book['price'], book['rating']))
    conn.commit()
    conn.close()