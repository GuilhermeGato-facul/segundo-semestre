notas = []

for i in range(6):
    nota = float(input(f"Digite a {i + 1}ª nota: "))
    notas.append(nota)

maior = max(notas)
menor = min(notas)
media = sum(notas) / len(notas)

acima_media = 0

for nota in notas:
    if nota > media:
        acima_media += 1

print(f"\nMaior nota: {maior}")
print(f"Menor nota: {menor}")
print(f"Média da turma: {media:.2f}")
print(f"Quantidade de notas acima da média: {acima_media}")