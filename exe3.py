matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor da posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

print("\nSoma de cada linha:")

soma_total = 0

for i in range(3):
    soma_linha = sum(matriz[i])
    print(f"Linha {i + 1}: {soma_linha}")
    soma_total += soma_linha

print(f"\nSoma total da matriz: {soma_total}")