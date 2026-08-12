from time import sleep

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
user = 0
while user != 5:
    print("""[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa""")
    user = int(input("Digite sua escolha: "))
    if user == 1:
        soma = n1 + n2
        print(f"A soma entre {n1} + {n2} é {soma}")
    elif user == 2:
        multi = n1 * n2
        print(f"A multiplicação entre {n1} * {n2} é {multi}")
    elif user == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f"O maior numero entre {n1} e {n2} é {maior}")
    elif user == 4:
        print("Informe os numeros novamente: ")
        n1 = int(input("Digite um numero: "))
        n2 = int(input("Digite outro numero: "))
    elif user == 5:
        print("Encerrando o programa!")
        print("-=" * 20)
        sleep(1)
    else:
        print("Opção invalida, tente novamente!")
    print("-="*20)
print("Programa encerrado!")