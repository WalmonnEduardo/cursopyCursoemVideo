from random import randint
from time import sleep
print('''Vamos jogar
[1]Pedra
[2]Papel
[3]Tesoura
''')
esc = int(input('Escolha: '))
c = randint(1,3)
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO\n')
if esc > 3 or esc < 1:
    print('Se tá doido, não tem essa opição')
else:
    if esc == 1:
        print('J:Pedra')
    elif esc == 2:
        print('J:Papel')
    else:
        print('J:Tesoura')
    if c == 1:
        print('C:Pedra')
    elif c == 2:
        print('C:Papel')
    else:
        print('C:Tesoura')
    if esc == c:
        print('Empate')
    elif esc == 1 and c == 2 or esc == 2 and c == 3 or esc == 3 and c == 1:
        print('Computador ganhou')
    else:
        print('Você ganhou')