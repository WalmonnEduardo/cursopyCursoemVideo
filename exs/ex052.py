n = int(input('Digite um número para vermos se ele é primo: '))
c = 0
for i in range(1,n+1):
    if n % i == 0:
        print('\033[35m',end=' ')
        c += 1
    else:
        print('\033[33m',end=' ')
    print(i)
if c == 2:
    print('\033[m0O número {0} foi dividido por {1}, então o número é primo'.format(n,c))
else:
    print('\033[m0O número {0} foi dividido por {1}, então o número não é primo'.format(n,c))