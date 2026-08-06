print("="*20)
print("PRIMEIROS 10 TERMOS DE UMA PA")
print("="*20)

# variaveis
p1 = int(input("Primeiro termo: "))
razao = int(input("Digite a razão: "))

for c in range(10):
        print(p1 + c * razao, "->",end = " ")
print("Acabou")


