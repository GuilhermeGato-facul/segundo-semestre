import sqlite3

from dominio.livro import Livro


class RepositorioLivro:

    def __init__(self, arquivo="biblioteca.db"):
        self.conexao = sqlite3.connect(arquivo)
        self.cursor = self.conexao.cursor()

    def _para_objeto(self, linha):
        codigo, titulo, autor, ano = linha

        livro = Livro(titulo, autor, ano)
        livro.id = codigo

        return livro

    def listar(self):
        self.cursor.execute(
            "SELECT id, titulo, autor, ano FROM livro"
        )

        return [
            self._para_objeto(linha)
            for linha in self.cursor.fetchall()
        ]

    def salvar(self, livro):
        self.cursor.execute(
            "INSERT INTO livro (titulo, autor, ano) VALUES (?, ?, ?)",
            (livro.titulo, livro.autor, livro.ano)
        )

        self.conexao.commit()

        livro.id = self.cursor.lastrowid

        return livro

    def buscar_por_id(self, codigo):
        self.cursor.execute(
            "SELECT id, titulo, autor, ano FROM livro WHERE id = ?",
            (codigo,)
        )

        linha = self.cursor.fetchone()

        if linha is None:
            return None

        return self._para_objeto(linha)

    def atualizar(self, livro):
        self.cursor.execute(
            "UPDATE livro SET titulo = ?, autor = ?, ano = ? WHERE id = ?",
            (
                livro.titulo,
                livro.autor,
                livro.ano,
                livro.id
            )
        )

        self.conexao.commit()

    def excluir(self, codigo):
        self.cursor.execute(
            "DELETE FROM livro WHERE id = ?",
            (codigo,)
        )

        self.conexao.commit()

    def fechar(self):
        self.conexao.close()