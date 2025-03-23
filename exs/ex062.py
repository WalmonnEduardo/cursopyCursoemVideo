print('Vamos fazer uma PA')
n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
i = 1
t = 0
m = 10
while m != 0:
    t += m
    while i <= t:
        print('{}'.format(n),end=' => ')
        n += r
        i += 1
    print('Pausa')
    m = int(input('Quantos termos você quer a mais: '))
print('Foram {0} termos mostrados'.format(t))