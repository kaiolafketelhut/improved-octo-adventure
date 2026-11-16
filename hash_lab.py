import hashlib, os, sqlite3

# --- 1. FALSCH: Klartext wie in test.db ---
print("--- FALSCH: Klartext ---")
print("admin : super-geheim-123  <- wenn DB geklaut, Game Over")

# --- 2. FALSCH: MD5 ohne Salt - in 1 Sekunde knackbar ---
print("\n--- FALSCH: MD5 ---")
print("bluh123 ->", hashlib.md5(b"bluh123").hexdigest())
print("Jeder kann das bei Google / crackstation nachschauen!")

# --- 3. RICHTIG: PBKDF2 + Salt ---
print("\n--- RICHTIG: PBKDF2 + Salt ---")

def hash_pass(password):
    salt = os.urandom(16)
    h = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return salt.hex() + ":" + h.hex()

def check_pass(password, stored):
    salt_hex, hash_hex = stored.split(":")
    salt = bytes.fromhex(salt_hex)
    h = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return h.hex() == hash_hex

# Gleiches Passwort, 2x gehasht = 2 verschiedene Hashes wegen Salt!
h1 = hash_pass("bluh123")
h2 = hash_pass("bluh123")
print("Hash 1:", h1[:40] + "...")
print("Hash 2:", h2[:40] + "...")
print("Gleiches Passwort, anderer Hash?", h1 != h2)
print("Richtiges Passwort?", check_pass("bluh123", h1))
print("Falsches Passwort?", check_pass("egal", h1))
