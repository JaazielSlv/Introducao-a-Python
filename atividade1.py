a = float(input("Valor 1: "))
b = float(input("Valor 2:"))
c = float(input("Valor 3: "))

delta = (b ** 2 - 4 * a * c)

if a == 0 or delta < 0: print("Impossivel calcular")
else:
    print('R1 = {:.5f}\n'.format(-b+(delta**(1/2)))/(2*a))
    print('R1 = {:.5f}\n'.format(-b-(delta**(1/2)))/(2*a))
