def ficha(nome='<desconhecido>',gols=0):
    print(f'O jogador {nome} fez {gols}')
nome = str(input('Digite o nome do jogador: ')).strip()
gols = str(input('Quantos gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome == '':
    ficha(gols=gols)
else:
    ficha(nome,gols)