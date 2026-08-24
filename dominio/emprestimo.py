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