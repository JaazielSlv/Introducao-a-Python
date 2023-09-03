cod = int(input("Qual codigo do lanche: ", ))
quant = int(input("Qual a Quantidade: "))
total = 0

lanche = ''

if (cod == 1): total = quant * 4.00
elif (cod == 2): total = quant * 4.5 
elif (cod == 3): total = quant * 5.0
elif (cod == 4): total = quant * 2.0
else: total = quant * 2.0

if (cod == 1): lanche = "Cachorro Quente"
elif (cod == 2): lanche = "X-Salada"
elif (cod == 3): lanche = "X-Bacon"
elif (cod == 4): lanche = "Torrada Simples"
else: lache = "Refrigerante"

print("Voçê Pediu", quant, lanche)    