import sqlite3


conn = sqlite3.connect('Bank.db')
c = conn.cursor()

def insertDeposit(amount):
    c.execute("CREATE TABLE IF NOT EXISTS deposits (id INTEGER PRIMARY KEY, amount REAL)")
    c.execute("INSERT INTO deposits (amount) VALUES (?)", (amount,))
    conn.commit()


def insertCharge(amount, description):
    c.execute("CREATE TABLE IF NOT EXISTS charges (id INTEGER PRIMARY KEY, amount REAL, description TEXT)")
    c.execute("INSERT INTO charges (amount, description) VALUES (?, ?)", (amount, description))
    conn.commit()

def getBalance():
    c.execute("SELECT SUM(amount) FROM deposits")
    total_deposits = c.fetchone()[0] or 0
    c.execute("SELECT SUM(amount) FROM charges")
    total_charges = c.fetchone()[0] or 0
    return total_deposits - total_charges