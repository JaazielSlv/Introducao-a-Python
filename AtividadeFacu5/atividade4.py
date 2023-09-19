n = int(input('Digite o total de experimentos: '))
scoelho = 0
srato = 0
ssapo = 0
for i in range(n):
    q = int(input('Quantia de cobaias: '))
    t = input('Tipo da cobaia: ')
    if(t == 'c'):
        scoelho = scoelho + q
    if(t == 'r'):
        srato = srato + q
    if(t == 's'):
        ssapo = ssapo + q
total = scoelho + srato + ssapo
print('cobaias', total)
print('{} coelhos \n{} ratos \n{} sapos '.format(scoelho,srato,ssapo))
print('Percentual de coelhos: {:.2f}%' .format((scoelho * 100) / total))
print('Percentual de ratos: {:.2f}% ' .format((srato * 100) / total))
print('Percentual de sapos: {:.2f}%' .format((ssapo * 100) / total))