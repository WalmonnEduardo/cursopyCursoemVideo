n = 0
for i in range(1,7):
    a = int(input('Digite um número: '))
    if a%2 == 0:
        n += a
print('A soma dos pares é {0}'.format(n))