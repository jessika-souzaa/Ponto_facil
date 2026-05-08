import sqlite3

def criar_banco():

    conexao = sqlite3.connect("database.db")
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        email TEXT,
        senha TEXT
        )
        """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pontos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT,
        nome TEXT,
        data TEXT,
        hora TEXT,
        tipo TEXT
        )
        """)

    conexao.commit()
    conexao.close()

if __name__ == "__main__":
    criar_banco()