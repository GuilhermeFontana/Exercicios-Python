total = maiorMil= cont = menor = 0
maisBarato = ""
while True:
    produto = str(input("Nome do produto: "))
    valor = float(input("Preço: R$"))
    cont += 1
    total += valor
    if valor > 1000:
        maiorMil += 1
    if cont == 1 or valor < menor:
        menor = valor
        maisBarato = produto
    continuar = " "
    while continuar not in "SN":
        continuar = input("Deseja continuar? [S/N] ").upper()
    if continuar == "N":
        break

print(f"O valor total da conta foi de R${total:.2f}")
print(f"Tivemos {maiorMil} produtos custando acima de R$1000.00")
print(f"O produto mais barato foi {maisBarato} custando R${menor:.2f}")