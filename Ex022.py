n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2) / 2

print(f"A media entre {n1} pontos e {n2} pontos tem o total de {media:.2f} pontos!")
if media >= 7:
    print("Você está aprovado!")
elif media >= 5 and media < 7:
    print("Você está de recuperação!")
else:
    print("Você está reprovado!")