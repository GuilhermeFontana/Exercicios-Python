

print("=-"*20)
print("LEITOR DE NUMERO PRIMO")
print("=-"*20)

num = int(input("Digite um numero inteiro: "))
cont = 0

for c in range (1, num+1):
    if num % c == 0:
        print("\033[34m", end="")
    else:
        print("\033[m", end="")
    print(f"{c}",end=" ")