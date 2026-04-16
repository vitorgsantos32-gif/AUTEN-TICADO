import os
from datetime import datetime

# Tenta usar MySQL primeiro, se falhar usa SQLite
USE_MYSQL = os.getenv('USE_MYSQL', 'false').lower() == 'true'

if USE_MYSQL:
    import mysql.connector
    from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME
    
    def conectar():
        """Conecta ao banco MySQL"""
        return mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
else:
    import sqlite3
    
    def conectar():
        """Conecta ao banco SQLite"""
        return sqlite3.connect('static/database.db')

def buscar_usuario(email):
    """Busca um usuário pelo email"""
    conn = conectar()
    
    if USE_MYSQL:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT id, email, senha, ativo, tentativas_login, ultimo_login FROM usuarios WHERE email = %s",
            (email,)
        )
        user = cursor.fetchone()
    else:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, email, senha, ativo, tentativas_login, ultimo_login FROM usuarios WHERE email = ?",
            (email,)
        )
        row = cursor.fetchone()
        user = {
            'id': row[0],
            'email': row[1],
            'senha': row[2],
            'ativo': row[3],
            'tentativas_login': row[4],
            'ultimo_login': row[5]
        } if row else None
    
    conn.close()
    return user

def atualizar_tentativas(email, tentativas):
    """Atualiza o número de tentativas de login"""
    conn = conectar()
    cursor = conn.cursor()
    
    if USE_MYSQL:
        cursor.execute(
            "UPDATE usuarios SET tentativas_login = %s WHERE email = %s",
            (tentativas, email)
        )
    else:
        cursor.execute(
            "UPDATE usuarios SET tentativas_login = ? WHERE email = ?",
            (tentativas, email)
        )
    
    conn.commit()
    conn.close()

def desativar_usuario(email):
    """Desativa um usuário"""
    conn = conectar()
    cursor = conn.cursor()
    
    if USE_MYSQL:
        cursor.execute(
            "UPDATE usuarios SET ativo = FALSE WHERE email = %s",
            (email,)
        )
    else:
        cursor.execute(
            "UPDATE usuarios SET ativo = 0 WHERE email = ?",
            (email,)
        )
    
    conn.commit()
    conn.close()

def atualizar_login(email):
    """Atualiza o último login do usuário"""
    conn = conectar()
    cursor = conn.cursor()
    
    if USE_MYSQL:
        cursor.execute(
            "UPDATE usuarios SET tentativas_login = 0, ultimo_login = %s WHERE email = %s",
            (datetime.now(), email)
        )
    else:
        cursor.execute(
            "UPDATE usuarios SET tentativas_login = 0, ultimo_login = ? WHERE email = ?",
            (datetime.now(), email)
        )
    
    conn.commit()
    conn.close()

def atualizar_senha(email, senha_hash):
    """Atualiza a senha do usuário"""
    conn = conectar()
    cursor = conn.cursor()
    
    if USE_MYSQL:
        cursor.execute(
            "UPDATE usuarios SET senha = %s, tentativas_login = 0, ultimo_login = %s WHERE email = %s",
            (senha_hash, datetime.now(), email)
        )
    else:
        cursor.execute(
            "UPDATE usuarios SET senha = ?, tentativas_login = 0, ultimo_login = ? WHERE email = ?",
            (senha_hash, datetime.now(), email)
        )
    
    conn.commit()
    conn.close()