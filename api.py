import uvicorn

from fastapi import FastAPI, HTTPException

from dados.repositorio_livro import RepositorioLivro


app = FastAPI()


def para_dict(livro):
    return {
        "id": livro.id,
        "titulo": livro.titulo,
        "autor": livro.autor,
        "ano": livro.ano,
    }


@app.get("/")
def inicio():
    return {"mensagem": "API da biblioteca"}


@app.get("/livros")
def listar_livros():
    repositorio = RepositorioLivro()

    livros = repositorio.listar()

    repositorio.fechar()

    return [para_dict(livro) for livro in livros]


@app.get("/livros/{codigo}")
def buscar_livro(codigo: int):
    repositorio = RepositorioLivro()

    livro = repositorio.buscar_por_id(codigo)

    repositorio.fechar()

    if livro is None:
        raise HTTPException(
            status_code=404,
            detail="Livro não encontrado"
        )

    return para_dict(livro)


if __name__ == "__main__":
    uvicorn.run(app)