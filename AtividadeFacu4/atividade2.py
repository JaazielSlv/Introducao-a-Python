segundo = int(input("QUANTIDADE DE SEGUNDOS: "))

horas = segundo // 3600
rhoras = segundo % 3600

minutos = rhoras // 60
rminutos = rhoras % 60

seg = rminutos % 60

print(horas, minutos, seg, sep=':')