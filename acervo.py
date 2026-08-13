def cadastrar(acervo, titulo, autor, ano):
    livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano
    }

    acervo.append(livro)


def buscar(acervo, titulo):
    for livro in acervo:
        if livro["titulo"].lower() == titulo.lower():
            return livro

    return None


def listar(acervo):
    return acervo


if __name__ == "__main__":
    acervo = []

    cadastrar(acervo, "Dom Casmurro", "Machado de Assis", 1899)

    print(buscar(acervo, "Dom Casmurro"))
    print(listar(acervo))

    acervo_vazio = []
    print(buscar(acervo_vazio, "Dom Casmurro"))