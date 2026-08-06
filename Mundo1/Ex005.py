import math
import random
from random import shuffle

# TIRAR AS VIRGULAS DE UM NUMERO (TRUNCAR)
# n1 = float(input("Digite um numero: "))
# result = math.trunc(n1)
# print(result)

# HIPOTENUSA
# co = int(input("Digite o valor do cateto oposto: "))
# ca = int(input("Digite o valor do cateto adjacente: "))
# hipotenusa = math.hypot(co, ca)
# print(f"O valor da hipotenusa é de {hipotenusa}")

# SENO, COSSENO, TANGENTE
# angulo = float(input("Digite o valor de um angulo: "))
# sen = math.sin(angulo)
# cos = math.cos(angulo)
# tan = math.tan(angulo)
# print(f"Seno {sen:.2f} \nCosseno {cos:.2f} \nTangente {tan:.2f}")

# n1 = str(input("Aluno 1: "))
# n2 = str(input("Aluno 2: "))
# n3 = str(input("Aluno 3: "))
#n4 = str(input("Aluno 4: "))
# nomes = random.choice([n1, n2, n3, n4])
# print("Nome para apagar quadro: ", nomes)


n1 = str(input("Aluno 1: "))
n2 = str(input("Aluno 2: "))
n3 = str(input("Aluno 3: "))
n4 = str(input("Aluno 4: "))
nomes = [n1,n2,n3,n4]
shuffle(nomes)
print(f"a ordem escolhida é: {nomes}")
