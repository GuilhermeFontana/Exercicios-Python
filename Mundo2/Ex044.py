c = 0
p1 = int(input("Digite o primeiro termo da sua PA: "))
razao = int(input("Digite a razão da sua PA: "))
while c < 10:
    print(p1 + c *razao, "-> ", end=" ")
    c = c + 1
print("acabou")