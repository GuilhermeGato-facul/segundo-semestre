from acervo import cadastrar, buscar, listar


def ler_ano():
    while True:
        try:
            return int(input("Ano de publicação: "))
        except ValueError:
            print("Digite um ano válido.")


def cadastrar_livro(acervo):
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = ler_ano()

    cadastrar(acervo, titulo, autor, ano)
    print("Livro cadastrado com sucesso!")


def consultar_livro(acervo):
    titulo = input("Título para consultar: ")
    livro = buscar(acervo, titulo)

    if livro:
        print("Título:", livro["titulo"])
        print("Autor:", livro["autor"])
        print("Ano:", livro["ano"])
    else:
        print("Livro não encontrado.")


def listar_livros(acervo):
    livros = listar(acervo)

    if not livros:
        print("O acervo está vazio.")
        return

    for livro in livros:
        print(
            f'{livro["titulo"]} - '
            f'{livro["autor"]} ({livro["ano"]})'
        )

    print("Total:", len(livros))


def main():
    acervo = []

    while True:
        print("\n1 - Cadastrar")
        print("2 - Consultar")
        print("3 - Listar")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_livro(acervo)
        elif opcao == "2":
            consultar_livro(acervo)
        elif opcao == "3":
            listar_livros(acervo)
        elif opcao == "4":
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()