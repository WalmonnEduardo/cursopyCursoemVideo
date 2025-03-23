print('Vamos fazer uma PA')
n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
i = 0
while i < 10:
    print('{}'.format(n),end=' => ')
    n += r
    i += 1
print('FIM')