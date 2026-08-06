l1 = float(input("Digite o primeiro segmento: "))
l2 = float(input("Digite o segundo segmento: "))
l3 = float(input("Digite o terceiro segmento: "))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l2 + l1:
    print(f"Os valores {l1}, {l2}, {l3}, podem formar um triangulo!")
    if l1 == l2 == l3:
        print("É um Triângulo Equilátero!")
    elif l1 != l2 and l2 != l3 and l3 != l1:
        print("É um Triângulo Escaleno")
    else:
        print("É um Triângulo Isósceles")
else:
    print(f"Os valores {l1}, {l2}, {l3}, NÃO podem formar um triangulo!")