l1 = float(input("Digite o primeiro segmento: "))
l2 = float(input("Digite o segundo segmento: "))
l3 = float(input("Digite o terceiro segmento: "))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l2 + l1:
    print(f"Os valores {l1}, {l2}, {l3}, podem formar um triangulo!")
else:
    print(f"Os valores {l1}, {l2}, {l3}, NÃO podem formar um triangulo!")