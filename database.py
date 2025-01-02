import sqlite3

def initialize_database():
    connection = sqlite3.connect("budget.db")
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date TEXT NOT NULL,
                        category TEXT NOT NULL,
                        amount REAL NOT NULL,
                        type TEXT NOT NULL CHECK(type IN ('income', 'expense'))
                      )''')
    connection.commit()
    connection.close()

def add_transaction(date, category, amount, type):
    connection = sqlite3.connect("budget.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO transactions (date, category, amount, type) VALUES (?, ?, ?, ?)",
                   (date, category, amount, type))
    connection.commit()
    connection.close()

def get_all_transactions():
    connection = sqlite3.connect("budget.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM transactions")
    rows = cursor.fetchall()
    connection.close()
    return rows

def delete_transaction(transaction_id):
    connection = sqlite3.connect("budget.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM transactions WHERE id = ?", (transaction_id,))
    connection.commit()
    connection.close()