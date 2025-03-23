print('='*50)
print(f'{' Super Baratão ':^50}')
print('='*50)
m = s = c = 0
m1000 = 0
while True:
    nome = str(input('Digite o nome do produto: ')).strip()
    preco = float(input('Digite o valor do produto: '))
    if c == 0:
        m = preco
        c += 1
    if preco < m:
        m = preco
        mbarato = nome
    if preco > 999:
        m1000 += 1
    s += preco
    print('='*50)
    while True:
        esc = str(input('Quer continuar[S/N]: ')).strip().upper()[0]
        if esc in 'SN':
            break
    if esc == 'N':
        print('='*50)
        break
    print('='*50)
print(f'A compra custa R${s:.2f}, {m1000} produtos custam mais de R$1.000,00 e o produto mais barato é {mbarato}')