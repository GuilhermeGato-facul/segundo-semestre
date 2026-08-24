class Livro:
    def __init__(self, titulo, autor, ano):
        if not titulo:
            raise ValueError("Titulo e obrigatorio")

        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, valor):
        if valor < 1450 or valor > 2026:
            raise ValueError(f"Ano invalido: {valor}")

        self._ano = valor

    def descricao(self):
        return f"{self.titulo} - {self.autor} ({self.ano})"

    def idade(self):
        return 2026 - self.ano

    def __str__(self):
        return self.descricao()