a = int(input("Valor A: "))
b = int(input("Valor B: "))

if (a > b): a, b = b, a
elif (b % a == 0): print(" São multiplos")
else:print("Não são Multiplos")


    