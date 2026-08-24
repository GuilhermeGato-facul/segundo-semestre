from dominio.livro import Livro
from dominio.usuario import Usuario
from dominio.emprestimo import Emprestimo


acervo = []
emprestimos = []

usuario = Usuario("Aluno", "0000")


while True:
    print()
    print("=== BIBLIOTECA ===")
    print("1 - Cadastrar livro")
    print("2 - Listar acervo")
    print("3 - Emprestar")
    print("0 - Sair")

    opcao = input("Opcao: ")


    if opcao == "1":
        titulo = input("Titulo: ")
        autor = input("Autor: ")

        try:
            ano = int(input("Ano: "))

            acervo.append(
                Livro(titulo, autor, ano)
            )

            print("Livro cadastrado.")

        except ValueError as erro:
            print("Nao deu:", erro)


    elif opcao == "2":
        if not acervo:
            print("Acervo vazio.")

        for livro in acervo:
            print("-", livro)


    elif opcao == "3":
        procurado = input("Titulo: ")
        escolhido = None

        for livro in acervo:
            if livro.titulo.lower() == procurado.lower():
                escolhido = livro

        if escolhido is None:
            print("Nao esta no acervo.")

        else:
            emprestimos.append(
                Emprestimo(
                    escolhido,
                    usuario,
                    "24/08/2026"
                )
            )

            print(
                "Emprestado:",
                emprestimos[-1]
            )


    elif opcao == "0":
        print("Ate logo.")
        break


    else:
        print("Opcao invalida.")