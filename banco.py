import sqlite3


conexao = sqlite3.connect("biblioteca.db")

cursor = conexao.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS livro (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT,
        ano INTEGER
    )
""")


print("Tabela criada.")


cursor.execute(
    "INSERT INTO livro (titulo, autor, ano) VALUES (?, ?, ?)",
    ("Dom Casmurro", "Machado de Assis", 1899),
)


print("Inserido.")


conexao.commit()


cursor.execute(
    "SELECT id, titulo, autor, ano FROM livro"
)


for codigo, titulo, autor, ano in cursor.fetchall():
    print(f"{codigo} - {titulo} - {autor} ({ano})")


conexao.close()