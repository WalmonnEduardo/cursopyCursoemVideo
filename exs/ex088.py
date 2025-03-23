from random import randint
print('-'*50)
print(f'{' Gerador de Jogos da Mega ':^50}')
print('-'*50)
j = int(input('Quantos jogos você quer fazer: '))
jogos = []
jogo = []
for i in range(j):
    while True:
        n = randint(1,60)
        if len(jogo) == 0:
            jogo.append(n)
        else:
            if n not in jogo:
                jogo.append(n)
        if len(jogo) == 6:
            jogo.sort()
            if jogo not in jogos:
                jogos.append(jogo[:])
            jogo.clear()
            break
for i in range(len(jogos)):
    print(f'Jogo {i+1}: {jogos[i]}')