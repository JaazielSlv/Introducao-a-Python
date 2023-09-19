v1=int(input("Valor 1: "))
v2=int(input("Valor 2: "))
soma = 0
if(v1>v2):
    v1,v2=v2,v1
    for i in range(v1 + 1,v2):
        if (i % 2)== 1:
            soma = soma + i
elif (v1<v2):
    for i in range(v1 + 1 ,v2):
        if (i % 2)== 1:
            soma = soma + i
print(soma)
