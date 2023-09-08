v1 = int(input("Valor 1: "))
v2 = int(input("Valor 2:"))
v3 = int(input("Valor 3: "))

if v1 > v2 > v3:print(v3,v2,v1)
if v2 > v1 > v3:print(v3,v1,v2)
if v3 > v2 > v1:print(v1,v2,v3)
if v2 > v3 > v1:print(v1,v3,v2)
if v1 > v3 > v2:print(v2,v3,v1)
if v3 > v1 > v2:print(v2,v1,v3)

print(v1,v2,v3)