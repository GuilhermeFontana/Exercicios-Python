salario = float(input("Digite o valor de seu salario: "))

if salario <= 1250:
    aumento = salario * (15/100)
    print(f"Voce recebera 15% de aumento\nO valor de seu salario agora é de R${salario+aumento:.2f}")
else:
    aumento = salario * (10/100)
    print(f"Voce recebera 10% de aumento\nO valor de seu salario agora é de R${salario + aumento:.2f}")