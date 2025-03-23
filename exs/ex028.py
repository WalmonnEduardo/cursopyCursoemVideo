from random import randint
from time import sleep
n = int(input('Digite um número: '))
print('Processando...')
sleep(3)
c = randint(0,5)
if n == c:
    print('Você ganhou!')
else:
    print('Você perdeu!\nEu você disse {0} e eu pensei {1}'.format(n,c))