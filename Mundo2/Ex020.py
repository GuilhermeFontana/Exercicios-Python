

n1 = int(input("Digite um numero para conversão: "))

print("1 - para binario \n2 - para octal\n3 - para hexadecimal")
escolha = int(input("Escolha uma das opções acima: "))

if escolha == 1 :
    print(bin(n1))
elif escolha == 2:
    print(oct(n1))
elif escolha == 3:
    print(hex(n1))
else:
    print("Opçao nao existe!")
