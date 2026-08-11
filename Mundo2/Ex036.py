from datetime import date

contadorM = 0
contador = 0
atual = date.today().year


for pess in range(1,8):
    idade = int(input(f"Em que ano a {pess} pessoa nasceu? "))
    soma = atual - idade
    if soma >= 18:
        contadorM = contadorM + 1
    else:
        contador = contador + 1

print(f"Já são maiores de idade {contadorM} pessoas!")
print(f"Ainda são menores de idade {contador} pessoas!")