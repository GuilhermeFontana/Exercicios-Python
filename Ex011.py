import random

print(f"{7*"-"} DESAFIO {7*"-"}")
npc = random.randrange(6)
n2 = int(input("Tente adivinhar o numero que a maquina pensou: "))
if n2 == npc:
    print(f"O numero que a maquina pensou foi {npc}")
    print(f"VOCÊ VENCEU!!!!!")
else:
    print(f"O numero que a maquina pensou foi {npc}")
    print(f"VOCÊ PERDEU!")