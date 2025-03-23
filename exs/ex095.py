from os import system
jogadores = list()
jogador = dict()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome: ')).strip()
    gols = list()
    q = 0
    partidas = int(input('Quantas partidas: '))
    for i in range(partidas):
        n = int(input(f'Gols no jogo {i}: '))
        q += n
        gols.append(n)
    jogador['gols'] = gols[:]
    jogador['quantidade'] = q
    jogadores.append(jogador.copy())
    while True:
        r = str(input('Deseja continuar[S/N]: ')).strip().upper()[0]
        if r in 'SN':
            break
    if r == 'N':
        break

while True:
    system('clear')
    print('cod',end=' | ')
    for i in jogador.keys():
        print(f'{i:<15}',end='  | ')
    print()
    print('-'*80)
    for k,v in enumerate(jogadores):
        print(f'{k:>3}',end=' | ')
        for d in v.values():
            print(f'{str(d):<15}',end='  | ')
        print()
    esc = int(input('Qual vc deseja especificar[999 para finalizar]: '))
    if esc == 999:
        break
    if len(jogadores) > esc > -1:
        system('clear')
        for k,v in jogadores[esc].items():
            if k != 'gols':
                print(f'{k}: {v}')
            else:
                m = 0
                for g in v:
                    print(f'Gols na partidade {m}: {g}')
                    m += 1
        input("'Aperte 'enter' para voltar")
    else:
        print(f'ERRO, não exite jogador na posição {esc}')
        input("'Aperte 'enter' para voltar")
system('clear')
print('Finalizado')