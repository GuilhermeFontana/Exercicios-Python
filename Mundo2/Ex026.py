valor = float(input("Digite o valor a ser pago: "))

print("[1] A vista dinheiro/Pix")
print("[2] A vista no cartão ")
print("[3] 2X no cartao")
print("[4] 3X ou mais")
opcao = int(input("Qual Opção? "))


if opcao == 1:
    desconto = valor - valor * (10/100)
    print(f"A vista no dinheiro/PIX recebe 10% de desconto, fica no total de R${desconto}")
elif opcao == 2:
    desconto = valor - valor * (5 / 100)
    print(f"A vista no cartão recebe 5% de desconto, fica no total de R${desconto}")
elif opcao == 3:
    print(f"O valor não muda, fica no total de R${valor}")
elif opcao == 4:
    parcelas = int(input("Quantas parcelas? "))
    conta = valor/parcelas
    juros = conta + conta*(20/100)
    print(f"Sua compra será parcelada em {parcelas}x de R${juros:.2f} com Juros. ")
    print(f"Sua compra de R${valor:.2f} vai custar R${parcelas*juros:.2f}")
else:
    print("Opçao nao existe!")