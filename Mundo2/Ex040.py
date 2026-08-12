from random import randrange

npc = randrange(11)
tentativas = 1

print("Olá sou seu computador, pensei em um numero entre 0 e 10\nTente adivinhar qual foi")
palpite = int(input("Digite o numero: "))

while palpite != npc:
    tentativas += 1
    if palpite > npc:
        palpite = int(input(f"É menor que {palpite}, digite outro numero: "))
    else:
        palpite = int(input(f"É maior que {palpite}, digite outro numero: "))
print(f"Voce acertou o numero {npc} em {tentativas} tentativas! Parabens! ")