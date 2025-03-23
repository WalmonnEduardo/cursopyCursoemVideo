n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))
nuns = (n1,n2,n3,n4)
print('Os valores da tupla são: ',end=' ')
for n in nuns:
    print(n,end=' ')
print(f'\nO valor 9 aparece {nuns.count(9)}')
print(f'O primeiro valor 3 foi digitado na posição {nuns.index(3)}') if 3 in nuns else print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares são: ',end='')
for n in nuns:
    if n % 2 == 0:
        print(n,end=' ')