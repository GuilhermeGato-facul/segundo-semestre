import tkinter as tk

from dominio.livro import Livro
from dominio.usuario import Usuario
from dominio.emprestimo import Emprestimo


acervo = [
    Livro("Dom Casmurro", "Machado de Assis", 1899),
    Livro("Iracema", "Jose de Alencar", 1865),
    Livro("O Cortico", "Aluisio Azevedo", 1890),
]

emprestimos = []

usuario = Usuario("Aluno", "0000")


janela = tk.Tk()
janela.title("Biblioteca")
janela.geometry("460x360")


tk.Label(
    janela,
    text="Acervo",
    font=("Arial", 14)
).pack(pady=6)


lista = tk.Listbox(
    janela,
    width=52,
    height=6
)

for livro in acervo:
    lista.insert(tk.END, str(livro))

lista.pack(padx=10)


campo = tk.Entry(
    janela,
    width=34
)

campo.pack(pady=8)


resultado = tk.Label(
    janela,
    text="",
    fg="blue"
)


def emprestar():
    procurado = campo.get()

    escolhido = None

    for item in acervo:
        if item.titulo.lower() == procurado.lower():
            escolhido = item

    if escolhido is None:
        resultado.config(
            text="Nao esta no acervo.",
            fg="red"
        )
        return

    emprestimo = Emprestimo(
        escolhido,
        usuario,
        "27/08/2026"
    )

    emprestimos.append(emprestimo)

    resultado.config(
        text="Emprestado: " + str(emprestimo),
        fg="blue"
    )


def devolver():
    if not emprestimos:
        resultado.config(
            text="Nao ha emprestimo.",
            fg="red"
        )
        return

    emprestimo = emprestimos[-1]

    try:
        emprestimo.devolver()

        resultado.config(
            text="Devolvido: " + str(emprestimo),
            fg="blue"
        )

    except ValueError as erro:
        resultado.config(
            text=str(erro),
            fg="red"
        )


tk.Button(
    janela,
    text="Emprestar",
    command=emprestar
).pack()


tk.Button(
    janela,
    text="Devolver",
    command=devolver
).pack(pady=4)


resultado.pack(pady=6)


janela.mainloop()