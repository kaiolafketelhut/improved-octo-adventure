import sqlite3

# Eigene Test-DB, nur auf deinem Handy!
db = sqlite3.connect('test.db')
c = db.cursor()
c.execute("DROP TABLE IF EXISTS users")
c.execute("CREATE TABLE users (name TEXT, pass TEXT)")
c.execute("INSERT INTO users VALUES ('admin', 'super-geheim-123')")
c.execute("INSERT INTO users VALUES ('bluh', 'bluh123')")
db.commit()

def login_vuln(name, password):
    # ABSICHTLICH unsicher - nur zum Lernen!
    query = f"SELECT * FROM users WHERE name='{name}' AND pass='{password}'"
    print(f"Query: {query}")
    c.execute(query)
    return c.fetchone()

print("--- Normal ---")
print(login_vuln("bluh", "bluh123"))
print("--- SQLi Angriff auf EIGENE DB ---")
print(login_vuln("' OR '1'='1", "egal"))
