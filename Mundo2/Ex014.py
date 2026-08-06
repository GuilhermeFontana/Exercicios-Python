km = float(input("Digite a distancia de sua viagem: "))

if km >= 200:
    print(f"O valor de sua viagem sai por R$0,45 por km\nDando um total de R${km*0.45:.2f}")
else:
    print(f"O valor de sua viagem sai por R$0,50 por km\nDando um total de R${km * 0.50:.2f}")