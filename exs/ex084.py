p = []
pessoas = []
while True:
    p.append(str(input('Nome: ')).strip())
    p.append(float(input('Peso: ')))
    pessoas.append(p[:])
    p.clear()
    while True:
        r = str(input('Quer continuar[S/N]: ')).strip().upper()[0]
        if r in 'SN':
            break
    if r == 'N':
        break
pesos = []
for pos,p in enumerate(pessoas):

    if pos == 0:
        min = p[1]
        leve = p[0]
        max = p[1]
    else:
        if p[1] > max:
            max = p[1]
            pesado = p[0]
        if p[1] < min:
            min = p[1]
leve = []
pesado = []
for i in pessoas:
    if i[1] == min:
        leve.append(i[0])
    if i[1] == max:
        pesado.append(i[0])
print(f'Tem {len(pessoas)} cadastradas')
print(f'As pessoas mais pesadas são {pesado} com {max}kg')
print(f'As pessoas mais leves são {leve} com {min}kg')