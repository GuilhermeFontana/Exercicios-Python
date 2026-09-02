print("FIBONACCI")
print("-="*20)
n1 = int(input("Quantos termos você quer mostrar? "))
c = 0
penultimo = -1
ultimo = 1

while c < n1:
    c += 1
    soma = penultimo + ultimo
    penultimo = ultimo
    ultimo = soma
    print(f"{soma}", end= " -> ")
print("Fim")