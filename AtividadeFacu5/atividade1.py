peca = int(input("Codigo da primeira peça: "))
quant = int(input("Quantidade de peças: "))
valor = float(input("Valor da Peça: "))

pecadois = int(input("Codigo da Segunda peça: "))
quantdois = int(input("Quantidade de peças: "))
valordois = float(input("Valor da Peça: "))


pagar = quant * valor
pagardois = quantdois * valordois

total = pagar + pagardois

print("VALOR A PAGAR: R${:.2f}".format(total))
