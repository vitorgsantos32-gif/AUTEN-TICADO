import sqlite3
from werkzeug.security import generate_password_hash

# Connect to SQLite database
conn = sqlite3.connect('static/database.db')
cursor = conn.cursor()

# Generate a valid password hash
hash_senha = generate_password_hash('teste')

# Create table and insert user
sql = """
CREATE TABLE IF NOT EXISTS usuarios ( 
   id INTEGER PRIMARY KEY AUTOINCREMENT, 
   email TEXT UNIQUE, 
   senha TEXT, 
   ativo INTEGER DEFAULT 1, 
   tentativas_login INTEGER DEFAULT 0, 
   ultimo_login TEXT 
);
"""

cursor.execute(sql)

cursor.execute(
    "INSERT OR REPLACE INTO usuarios (email, senha, ativo, tentativas_login, ultimo_login) VALUES (?, ?, ?, ?, ?)",
    ('admin@gmail.com', hash_senha, 1, 0, None)
)

conn.commit()
conn.close()

print("✅ Banco de dados SQLite criado/atualizado com sucesso!")