contador = 1
media = 0
opcao = str("s")

numero = int(input("Digite um numero: "))
maior = numero
menor = numero
soma = numero
opcao = str(input("Quer continuar? [S/N] ")).lower()
while opcao != "n":
    numero = int(input("Digite um numero: "))
    contador += 1
    soma += numero
    media = soma /contador
    opcao = str(input("Quer continuar? [S/N] ")).lower()
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print(f"Voce digitou {contador} numeros e a média foi {media:.2f}")
print(f"O maior numero foi {maior} e o menor foi {menor}")