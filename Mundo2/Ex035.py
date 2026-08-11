
palavra = str(input("Digite uma frase ou palavra: ")).upper().replace(" ", "")
invertido = ""
for c in palavra:
    invertido = c + invertido
print(f"{invertido}")
if palavra == invertido:
    print(f"A palavra {palavra} é um Palindromo")
else:
    print(f"A palavra {palavra} não é um Palindromo")