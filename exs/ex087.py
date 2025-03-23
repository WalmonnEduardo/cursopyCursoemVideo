matriz = []
vetor = []
pares = 0
terc = 0
for i in range(3):
    for j  in range(3):
        n = int(input(f'Digite um valor para colocar na posição[{i}][{j}]: '))
        if n % 2 == 0:
            pares += n
        if i == 2:
            terc += n
        vetor.append(n)
    matriz.append(vetor[:])
    vetor.clear()
m = 0
for j in matriz:
    for i in j:
        if i > m:
            m = i
n = str(m)
a = len(n)
print('Sua matriz ficou asssim')
for l in matriz:
    for p in l:
        print(f'[{p:^{a}}]',end='')
    print()
print(f'A soma dos números pares são {pares}')
print(f'A soma de valores da terceira coluna é {terc}')
print(f'O maior valor da segunda coluna é {max(matriz[1])}')