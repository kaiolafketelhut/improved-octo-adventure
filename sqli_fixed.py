import sqlite3
db = sqlite3.connect('test.db')
c = db.cursor()

def login_fixed(name, password):
    # FIX: ? Platzhalter, kein f-string!
    c.execute("SELECT * FROM users WHERE name=? AND pass=?", (name, password))
    return c.fetchone()

print("--- Normal, geht ---")
print(login_fixed("bluh", "bluh123"))
print("--- SQLi, geht NICHT mehr ---")
print(login_fixed("' OR '1'='1", "egal"))
