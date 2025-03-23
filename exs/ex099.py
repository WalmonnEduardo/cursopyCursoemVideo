def maior(*nuns):
    print('Analisando os valores passados: ',end='')
    if len(nuns) > 0:
        c = 0
        for i in nuns:
            print(i,end=' ')
            if c == 0:
                maior = i
            if i > maior:
                maior = i
            c += 1
        print()
        print(f'Foi informado {len(nuns)} e o maior valor informado foi {maior}')
    else:
        print('Não foi informado valores!')
maior(3,2,4,5,2,1,4)
maior(3,2,4,5)
maior(3)
maior()