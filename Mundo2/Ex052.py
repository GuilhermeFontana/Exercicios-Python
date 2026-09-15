maisDezoito = 0
homens = 0
mulherMenosVinte = 0

print("-"* 20)
print("CADASTRO DE PESSOAS")
print("-"* 20)

while True:
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo: [M/F] ")).upper()

    c = " "
    while c not in "SN":
        c = str(input("Quer continuar: [S/N] ")).upper()

    print("-" * 20)

    if idade > 18:
        maisDezoito += 1
    if sexo == "M" or "F":
        if sexo == "F" and idade < 20:
            mulherMenosVinte +=1
        if sexo == "M":
            homens += 1
    if c == "N":
        break

print(f"Possui no cadastro {maisDezoito} pessoas com mais de 18 anos.")
print(f"Possui no cadastro {mulherMenosVinte} mulheres com menos de 20 anos.")
print(f"Possui no cadastro {homens} homens.")