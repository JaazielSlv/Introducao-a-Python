valor=int(input("Digite o valor: "))

for i in range(1, 10000):
    if i % valor == 2:
        print(i)