soma = 0

for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número: "))
    soma += numero

media = soma / 5

print(f"\nSoma = {soma}")
print(f"Média = {media}")