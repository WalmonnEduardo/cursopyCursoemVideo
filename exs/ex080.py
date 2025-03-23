nuns = []
for i in range(5):
    n = int(input('Digite um valor: '))
    if i == 0:
        nuns.append(n)
        print('Número adicionado no final!')
    else:
        if n not in nuns:
            for j in range(len(nuns)):
                if n < nuns[j]:
                    nuns.insert(j, n)
                    print(f'Número adicionado na posição {j}')
                    break
                if j == len(nuns) - 1 and n > nuns[j]:
                    nuns.append(n)
                    print('Número adicionado no final!')
        else:
            print('O valor não pode ser adicionado por ser repetido!')
print(f'A lista ficou assim: {nuns}')