from dominio.livro import Livro
from dados.repositorio_livro import RepositorioLivro


repositorio = RepositorioLivro()


print("--- guardando um livro novo ---")

novo = Livro(
    "Memorias Postumas",
    "Machado de Assis",
    1881
)

repositorio.salvar(novo)

print("guardado com o id", novo.id)


print("--- buscando so ele ---")

achado = repositorio.buscar_por_id(novo.id)

print(
    "achei:",
    achado,
    "- tipo:",
    type(achado).__name__
)


print("--- corrigindo o titulo ---")

achado.titulo = "Memorias Postumas de Bras Cubas"

repositorio.atualizar(achado)

print(
    "agora:",
    repositorio.buscar_por_id(novo.id)
)


print("--- apagando ---")

repositorio.excluir(novo.id)

print(
    "procurando de novo:",
    repositorio.buscar_por_id(novo.id)
)


repositorio.fechar()