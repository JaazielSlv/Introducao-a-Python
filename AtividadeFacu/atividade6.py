# consumo = d(distância total em Km) / c(combustível gasto)

d = float(input("distância total em Km: "))
c = float(input("combustível gasto: "))

consumo = d / c

print("{:.3f} km/l".format(consumo))
