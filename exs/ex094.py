pessoas = list()
pessoa = dict()
media = 0
m = 0
while True:
    pessoa['nome'] = str(input('Nome: ')).strip()
    pessoa['idade'] = int(input('Idade: '))
    media += pessoa['idade']
    while True:
        s = str(input('Sexo[M/F]: ')).strip().upper()[0]
        if s in 'MF':
            break
    if s == 'F':
        m += 1
    pessoa['sexo'] = s
    pessoas.append(pessoa.copy())
    while True:
        r = str(input('Deseja continuar[S/N]: ')).strip().upper()[0]
        if r in 'SN':
            break
    if r == 'N':
        break
media /= len(pessoas)
print(f'Tem {len(pessoas)} pessoas')
print(f'Média da idade das pessoas é {media}')
if m > 0:
    print('As mulheres são ',end='')
    for p in pessoas:
        for k,v in p.items():
            if k == 'nome':
                nome = v
            if k == 'sexo' and v == 'F':
                print(nome,end=' ')
else:
    print('Não tem mulheres')
print('\nAs pessoas acima da média são ',end='')
for i in range(len(pessoas)):
    if pessoas[i]['idade'] > media:
        print(pessoas[i]['nome'],end=' ')