# Salarido = d(dias trabalhados) * h(horas trabalhadas) * vl(Valor por Hora trabalhada) 

d = float(input("Quantidade de dias de trabalho: ")) 
h = float(input("Quantidade de horas trabalhadas: ")) 
vl = float(input("Valor por Hora Trabalhada: "))

salario = vl * h 

print("Numero:", d)
print("salario: U$ {:.2f}".format(salario))
