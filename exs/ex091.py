from random import randint
from operator import itemgetter 
jogo = {
    'jogador 1':randint(1,6),
    'jogador 2':randint(1,6),
    'jogador 3':randint(1,6),
    'jogador 4':randint(1,6)
}
m = 1
ranking = sorted(jogo.items(),key=itemgetter(1),reverse=True)
for k,v in enumerate(ranking):
    print(f'{m}° lugar = {v[0]} tirou {v[1]}')
    m += 1