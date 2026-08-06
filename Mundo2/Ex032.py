soma = 0

for c in range(1, 7):
    numeros = int(input("Digite um numero: "))
    if numeros % 2 == 0:
         soma = soma + numeros
print(f"A soma dos numeros pares digitados sao {soma}")