class Livro:
    def __init__(self, titulo, autor, ano):
        if not titulo:
            raise ValueError("Titulo e obrigatorio")

        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def descricao(self):
        return f"{self.titulo} - {self.autor} ({self.ano})"

    def idade(self):
        return 2026 - self.ano

    def __str__(self):
        return self.descricao()

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, valor):
        if valor < 1450 or valor > 2026:
            raise ValueError(f"Ano invalido: {valor}")

        self._ano = valor


class Usuario:
    def __init__(self, nome, matricula):
        if not nome:
            raise ValueError("Nome e obrigatorio")

        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} ({self.matricula})"


class Emprestimo:
    def __init__(self, livro, usuario, data):
        self.livro = livro
        self.usuario = usuario
        self.data = data
        self.devolvido = False

    def devolver(self):
        if self.devolvido:
            raise ValueError("Este emprestimo ja foi devolvido")

        self.devolvido = True

    def __str__(self):
        estado = "devolvido" if self.devolvido else "em aberto"
        return f"{self.livro.titulo} -> {self.usuario.nome} ({estado})"


if __name__ == "__main__":
    livro = Livro("Dom Casmurro", "Machado de Assis", 1899)

    print(livro)

    try:
        livro.ano = 3000
    except ValueError as erro:
        print(erro)

    print(livro.ano)

    ana = Usuario("Ana Souza", "2026001")
    emp = Emprestimo(livro, ana, "20/08/2026")

    print(emp)

    print(emp.livro.autor)
    print(emp.usuario.matricula)

    emp.devolver()
    print(emp)

    emp.devolver()