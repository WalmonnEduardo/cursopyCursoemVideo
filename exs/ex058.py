from random import randint 
v = randint(0,10)
t = 0
print('Estou pensando em um número entre 0 e 10')
a = False
while not a:
    j = int(input('Tente adivinhar: '))
    if v == j:
        a = True
    elif j > v:
        print('O valor é menor')
    else:
        print('O valor é maior')
    t += 1
print('Parabéns, você acerto com {} tentativas'.format(t))