nuns = []
par = []
impar = []
while True:
    n = int(input('Digite um número: '))
    nuns.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    while True:
        r = str(input('Deseja continuar[S/N]: ')).strip().upper()[0]
        if r in 'SN':
            break
    if r == 'N':
        nuns.sort()
        par.sort()
        impar.sort()
        break
print(f'Os números digitados foram: {nuns}')
print(f'Os pares são: {par}')
print(f'Os ímpares são {impar}')