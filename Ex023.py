import datetime

# variaveis
ano = int(input("Digite o ano de nascimento: "))
atual = datetime.datetime.today().year
idade = atual - ano

# classificação
print(f"O atleta possui {idade} anos.")
if  idade <= 9:
    print("Classificação: Mirim.")
elif idade <= 14:
    print("Classificação: Infantil.")
elif idade <= 19:
    print("Classificação: Junior.")
elif idade <= 25:
    print("Classificação: Sênior.")
else:
    print("Classificação: Master.")