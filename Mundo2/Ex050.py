print("-="*20)
print("Programa Tabuada")
print("-="*20)

while True:

    n = int(input("Deseja a tabuada de qual valor? "))
    if n < 0:
        break
    print("-=" * 20)
    for c in range (0, 11):
        m = c*n
        print(f"{n} X {c} = {m}")
    print("-=" * 20)
print("-=" * 20)
print("Encerrando o programa volte sempre!!!")