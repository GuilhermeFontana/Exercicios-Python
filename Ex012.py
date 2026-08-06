
velocidade = int(input("Digite a velocidade do carro: "))
if velocidade > 80:
    multa = (velocidade - 80) * 7.00
    print("Voce ultrapassou o limite da via! Foi multado!")
    print(f"Valor da multa R${multa}")
else:
    print("Parabéns por andar no limite da via continue assim!")