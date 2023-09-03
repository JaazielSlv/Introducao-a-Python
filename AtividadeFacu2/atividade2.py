x = float(input("Valor de X: "))
y = float(input("Valor de Y: "))
coordenada = 0

if (x > 0) & (y > 0): coordenada = "Q1"
elif (x < 0) & (y > 0): coordenada = "Q2"
elif (x < 0) & (y < 0): coordenada = "Q3"
elif (x > 0) & (y < 0): coordenada = "Q4"
else: coordenada = "origem"

print(coordenada)