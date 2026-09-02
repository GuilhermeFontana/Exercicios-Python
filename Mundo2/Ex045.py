from time import sleep
print("Gerador De PA")
print("-="* 10)

p1 = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
termo = p1
cont = 0
resposta = 10
while resposta != 0:
   for x in range(resposta):
        print(f"{termo} -> ", end ="")
        termo += razao
        resposta += resposta
   print("Pausa")
   resposta = int(input("Quantos termos voce quer mostrar a mais? "))
sleep(1)
print("Encerrando programa")