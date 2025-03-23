matriz = []
vetor = []
for i in range(3):
    for j  in range(3):
        n = int(input(f'Digite um valor para colocar na posição[{i}][{j}]: '))
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