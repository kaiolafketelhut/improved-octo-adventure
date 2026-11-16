import hashlib, os, sqlite3

db = sqlite3.connect('secure.db')
c = db.cursor()
c.execute("DROP TABLE IF EXISTS users")
c.execute("CREATE TABLE users (name TEXT, hash TEXT)")
db.commit()

def hash_pass(pw):
    salt = os.urandom(16)
    h = hashlib.pbkdf2_hmac('sha256', pw.encode(), salt, 100000)
    return salt.hex() + ":" + h.hex()

def register(name, pw):
    # FIX 1: ? Platzhalter gegen SQLi
    c.execute("INSERT INTO users VALUES (?, ?)", (name, hash_pass(pw)))
    db.commit()

def login(name, pw):
    # FIX 1: ? Platzhalter gegen SQLi
    c.execute("SELECT hash FROM users WHERE name=?", (name,))
    row = c.fetchone()
    if not row: return False
    # FIX 2: Hash vergleichen, nie Klartext
    salt_hex, hash_hex = row[0].split(":")
    h = hashlib.pbkdf2_hmac('sha256', pw.encode(), bytes.fromhex(salt_hex), 100000)
    return h.hex() == hash_hex

register("bluh", "bluh123")
print("Richtig:", login("bluh", "bluh123"))
print("Falsch:", login("bluh", "egal"))
print("SQLi:", login("' OR '1'='1 -- ", "egal"))
print("SQLi 2:", login("bluh", "' OR '1'='1"))
