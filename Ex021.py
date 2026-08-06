import datetime

# variaveis
sexo = str(input("Qual é seu sexo? ")).lower()
if sexo == "masculino":
    nascimento = int(input("Digite o ano que voce nasceu: "))
    atual = datetime.date.today().year
    idade = atual - nascimento

    print(f"Quem nasceu em {nascimento} tem {idade} anos em {atual} ")
    if idade == 18:
        print("Voce tem 18 anos! precisa se alistar imediatamente")
    elif idade < 18:
        saldo = 18 - idade
        print(f"Você ainda é muito novo, faltam {saldo} anos para seu alitamento")
        print(f"seu ano de alistamento é em {nascimento + 18}")
    else:
        saldo = idade - 18
        print(f"O seu ano de alistamento ja passou!!\nprecisava ter se alistado em {nascimento + 18}\ndeveria ter se alistado {saldo} anos atras!")
else:
    print("alistamento somente para o SEXO masculino! ")