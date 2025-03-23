from datetime import date
me = 0
ma = 0
for i in range(7):
    ano = int(input('Digite seu ano de nascimento pessoa {}°: '.format(i+1)))
    if date.today().year - ano >= 18:
        ma += 1
    else:
        me += 1
print('São {0} pessoas maiores de idade, e {1} pessoas menores de idade.'.format(ma,me))