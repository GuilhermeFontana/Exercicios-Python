peso = float(input("Digite seu peso em kgs: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura * altura)

print(f"O seu IMC é de {imc:.2f}")

if  imc <= 18.5:
    print("Classificação: Magreza.")
elif imc <= 24.9:
    print("Classificação: Peso normal.")
elif imc <= 29.9:
    print("Classificação: Sobrepeso.")
elif imc <= 39.9:
    print("Classificação: Obesidade.")
else:
    print("Classificação: Obesidade mórbid"
          "a.")