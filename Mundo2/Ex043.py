
produto= 1
n1 = int(input("Digite um numero: "))
print(f"Calculando {n1}! = ", end = "")
for c in range(1,n1+1):
    produto = produto * c
print(produto)