class Usuario:
    def __init__(self, nome, matricula):
        if not nome:
            raise ValueError("Nome e obrigatorio")

        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} ({self.matricula})"