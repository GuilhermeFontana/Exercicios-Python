somaidade = 0
mediaIdade = 0
maioridadehomem = 0
nomemaisvelho = ""
contadorMulher = 0

for p in range(1, 5):
    print(f"-----{p}º Pessoa -----")
    nome = str(input("Nome: ")).strip()
    idade = int(input("idade: "))
    sexo = str(input("sexo [M/F]: ")).strip()
    somaidade += idade
    if p == 1 and sexo in "Mm":
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in "Mm" and idade>maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome
    if idade < 20 and sexo in "Ff":
        contadorMulher +=1

mediaIdade = somaidade/4
print(f"A media de idade do grupo é de {mediaIdade} anos! ")
print(f"O homem mais velho se chama {nomemaisvelho} e tem {maioridadehomem} anos")
print(f"A quantidade de mulheres com menos de 20 anos é: {contadorMulher}")