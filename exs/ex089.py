from os import system
lista = []
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    m = ( n1 + n2 ) / 2
    ficha = [nome,[n1,n2],m]
    lista.append(ficha[:])
    while True:
        r = str(input('Deseja continuar[S/N]: ')).strip().upper()
        if r in 'SN':
            break
    if r == 'N':
        break
    ficha.clear()
system('clear')
for aluno in lista:
    print(50*'-')
    print(f'Nome: {aluno[0]}')
    print(f'Nota 1: {aluno[1][0]}')
    print(f'Nota 2: {aluno[1][1]}')
    print(f'Média: {aluno[2]}')