n1 = float(input('Digite o primeiro seguimento: '))
n2 = float(input('Digite o segundo seguimento: '))
n3 = float(input('Digite o terceiro seguimento: '))
if (n1+n2) > n3:
    if (n1+n3) > n2:
        if (n2+n3) > n1:
            print('Os seguimentos podem formar um triângulo.')
        else:
            print('Os seguimentos não podem formar um triângulo')
    else:
        print('Os seguimentos não podem formar um triângulo')
else:
    print('Os seguimentos não podem formar um triângulo')