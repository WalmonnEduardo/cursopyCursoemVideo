n1 = float(input('Digite o primeiro seguimento: '))
n2 = float(input('Digite o segundo seguimento: '))
n3 = float(input('Digite o terceiro seguimento: '))
if (n1+n2) > n3 and (n1+n3) > n2 and (n2+n3) > n1:
    print('Os seguimentos podem formar um triângulo.')
    if n1 == n2 and n1 == n3:
        print('Equilátero!')
    elif n1 == n2 or n1 == n3  or n2 == n3:
        print('Isósceles')
    else:
        print('Escaleno')
else:
    print('Os seguimentos não podem formar um triângulo')