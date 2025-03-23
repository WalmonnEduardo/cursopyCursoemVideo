from os import system
jogador = dict()
jogador['nome'] = str(input('Nome: ')).strip()
gols = list()
q = 0
for i in range(4):
    n = int(input(f'Gols no jogo {i}: '))
    q += n
    gols.append(n)
jogador['gols'] = gols[:]
jogador['quatidade'] = q
system('clear')
for k,v in jogador.items():
    if k != 'gols':
        print(f'{k}: {v}')
    else:
        m = 0
        for g in v:
            print(f'Gols na partidade {m}: {g}')
            m += 1