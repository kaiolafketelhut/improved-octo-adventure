import sqlite3
db = sqlite3.connect('test.db')
c = db.cursor()

def login_vuln(name, password):
    query = f"SELECT * FROM users WHERE name='{name}' AND pass='{password}'"
    print(f"Query: {query}")
    c.execute(query)
    return c.fetchone()

def login_fixed(name, password):
    c.execute("SELECT * FROM users WHERE name=? AND pass=?", (name, password))
    return c.fetchone()

print("--- VULN mit -- Bypass ---")
# -- macht den Rest der Zeile zu einem Kommentar, Passwort wird ignoriert!
print(login_vuln("' OR '1'='1' -- ", "egal"))
print("--- FIXED mit gleichem Bypass ---")
print(login_fixed("' OR '1'='1' -- ", "egal"))
