from random import randint
from time import sleep

itens = ("Pedra", "Papel", "Tesoura")
pc = randint(0, 2)
print("""Suas Opções: 
[0] Pedra
[1] Papel
[2] Tesoura""")
usuario = int(input("Qual a sua escolha? "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!!")
sleep(1)
print("-=" * 15)
print(f"O computador jogou {itens[pc]}")
print(f"O usuario jogou {itens[usuario]}")
print("-=" * 15)

if pc == 0:
    if usuario == 0:
        print("Empate!")
    elif usuario == 1:
        print("O usuario venceu!")
    elif usuario == 2:
        print("A maquina venceu!")
elif pc == 1:
    if usuario == 0:
        print("O usuario perdeu!")
    elif usuario == 1:
        print("Empate!")
    elif usuario == 2:
        print("O Usuario venceu")
elif pc == 2:
    if usuario == 0:
        print("O Usuario venceu!")
    elif usuario == 1:
        print("A Maquina venceu!")
    elif usuario == 2:
        print("Empate!")
else:
    print("opcao nao existe!")