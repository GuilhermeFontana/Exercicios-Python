contador = 0
soma = 0
c = int(input("Digite um valor [999 para parar]: "))
while c != 999:
    contador += 1
    soma += c
    c = int(input("Digite um valor [999 para parar]: "))

print(f"Foi digitado {contador} numeros e a soma entre eles é {soma}")
