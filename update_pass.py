import sqlite3
from werkzeug.security import generate_password_hash

conn = sqlite3.connect('static/database.db')
cursor = conn.cursor()

hash_senha = generate_password_hash('teste')
cursor.execute("UPDATE usuarios SET senha = ? WHERE email = ?", (hash_senha, 'admin@gmail.com'))

conn.commit()
conn.close()

print("Password updated to 'teste'.")