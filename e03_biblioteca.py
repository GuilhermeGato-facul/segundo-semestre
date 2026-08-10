
# Encontro 3 - Dicionário e Acervo
# Programação para Desktop e Web

acervo = []

while True:
    print("\n===== BIBLIOTECA =====")
    print("1 - Cadastrar")
    print("2 - Consultar")
    print("3 - Listar")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        ano = int(input("Digite o ano do livro: "))

        livro = {
            "titulo": titulo,
            "autor": autor,
            "ano": ano
        }

        acervo.append(livro)

        print("Livro cadastrado.")

    elif opcao == "2":
        titulo_procurado = input("Digite o título para consultar: ")

        encontrado = False

        for livro in acervo:
            if livro["titulo"] == titulo_procurado:
                print(f"Autor: {livro['autor']}")
                print(f"Ano: {livro.get('ano', 'ano desconhecido')}")
                encontrado = True
                break

        if not encontrado:
            print("Nao esta no acervo.")

    elif opcao == "3":
        if len(acervo) == 0:
            print("Acervo vazio.")
        else:
            for livro in acervo:
                print(
                    f"{livro['titulo']} "
                    f"({livro.get('ano', 'ano desconhecido')}) - "
                    f"{livro['autor']}"
                )

            print(f"Total: {len(acervo)} livros.")

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Tente novamente.")


# Respostas da Parte 4:
# 1. O que impede você de criar um livro sem ano?
# O programa pede o ano e usa int() para cadastrar o livro.

# 2. O que impede alguém de escrever "ano": "mil oitocentos"?
# Nada neste programa impede; seria necessário validar o tipo do ano.

# 3. Se amanhã todo livro precisar de editora, em quantos lugares do seu código você tem que mexer?
# Será necessário alterar o cadastro e os pontos onde os dados do livro são tratados.
