hi=int(input('Digite o valor da hora inicial '))
hf=int(input('Digite o valor da hora final '))

if hi==hf:print('O jogo durou 24 Horas')
else:
    if hi<hf:print('O jogo durou',hf-hi,'Hora (S)')
    else:    
        if hi>hf:print('O jogo durou',(24-hi)+hf, 'Hora (S)')
