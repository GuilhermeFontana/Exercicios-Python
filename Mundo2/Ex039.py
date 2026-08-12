sexo = str(input("Digite seu sexo [M/F]: ")).strip().upper()[0]
while sexo not in "MmFf":
    sexo = str(input("Dados invalidos. Digite seu sexo [M/F]: ")).strip().upper()[0]
print("Os dados batem, pode entrar!")