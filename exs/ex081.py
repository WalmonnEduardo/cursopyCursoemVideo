nuns = []
c = 0
while True:
    n = int(input('Digite um número: '))
    nuns.append(n)
    c += 1
    while True:
        r = str(input('Deseja continuar[S/N]: ')).strip().upper()[0]
        if r in 'SN':
            break
    if r == 'N':
        break
print(f'Fora adicionados {c} números')
nuns.sort(reverse=True)
print(f'A lista em ordem decrescente é {nuns}')
print('O número 5 está na lista') if 5 in nuns else print('O número 5 não está na lista')