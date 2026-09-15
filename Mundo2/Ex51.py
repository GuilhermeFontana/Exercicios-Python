from random import randrange
v = 0

while True:
    print("=-" * 10)
    jogador = int(input("Diga um valor: "))
    escolha = " "
    while escolha not in "PI":
        escolha = str(input("Par ou impar? [P/I] ")).upper()
    pc = randrange(11)
    print("=-"*10)
    if escolha == "P":
       if (jogador + pc) % 2 == 0:
           print(f"A maquina escolheu {pc}")
           print("Voce venceu! ")
           print("Vamos continuar!")
           v += 1
       else:
           print(f"A maquina escolheu {pc}")
           print("Você foi derrotado!")
           break
    elif escolha == "I":
        if (jogador + pc) % 2 == 0:
            print(f"A maquina escolheu {pc}")
            print("Você foi derrotado!")
            break
        else:
            print(f"A maquina escolheu {pc}")
            print("Voce venceu! ")
            print("Vamos continuar!")
            v += 1
    else:
        print("Escolha nao existe!!")

print("=-" * 10)
print(f"Voce venceu a maquina por {v} vezes!")
