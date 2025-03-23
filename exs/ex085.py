nuns = [[],[]]
for i in range(7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        if len(nuns[0]) == 0 or n > nuns[0][-1]:
            nuns[0].append(n)
        else:
            for pos , p in enumerate(nuns[0]):
                if n > p:
                    nuns[0].insert(pos,n)
    else:
        if len(nuns[1]) == 0 or n > nuns[1][-1]:
            nuns[1].append(n)
        else:
            for pos , p in enumerate(nuns[1]):
                if n > p:
                    nuns[1].insert(pos,n)
print(f'A lista de pares é {nuns[0]}')
print(f'A lista de números ímpares é {nuns[1]}')

