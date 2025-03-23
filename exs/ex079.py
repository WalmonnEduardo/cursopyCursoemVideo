nuns = []
c = 0
while True:
    n = str(input('Digite um valor: '))
    if n.isnumeric():
        n = int(n)
        if n in nuns:
            print('Valor duplicado não, poderei adicionar!')
        else:
            nuns.append(n)
            c += 1
            print('Valor adicionado com sucesso!')
    else:
        print('Valor não inteiro, não poderei adicinar!')
    while True:
        s = str(input('Deseja continuar[S/N]: ')).strip().upper()[0]
        if s in 'SN':
           break
    if s == 'N':
        break
if c > 0:
    nuns.sort()
    print(f'A lista ficou assim: {nuns}')
else:
    print('Não adicionou nada')