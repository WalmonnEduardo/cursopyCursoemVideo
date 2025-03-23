d = float(input('Digite a distância da viagem em km: '))
print('Você está preste a começar uma viagem de {:.2f}km'.format(d))
if d > 200:
    p = d * 0.45
    print('O valor da passagem será R${:.2f}'.format(p))
else:
    p = d * 0.5
    print('O valor da passagem será R${:.2f}'.format(p))
p = d*0.5 if d <= 200 else d*0.45
print('O valor da passagem será R${:.2f}'.format(p))