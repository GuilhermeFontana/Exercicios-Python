print(10*"-", "Calculo emprestimo", 10*"-")
vCasa = float(input("Digite o valor da casa: "))
vSalario = float(input("Digite o valor do seu salario: "))
tempo = int(input("Dite o tempo em anos que gostaria de pagar: "))
vPrestacao = vCasa / (tempo*12)
if vPrestacao > vSalario * (30/100):
    print("O valor da prestação excede seu limite! EMPRESTIMO NEGADO! ")
else:
    print(f"O valor da prestação ficou em R${vPrestacao:.2f} e vai ser pago em {tempo} anos")