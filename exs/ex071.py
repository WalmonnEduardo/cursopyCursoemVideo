print('='*50)
print(f'{' Caixa do Banco ':^50}')
print('='*50)
sac = int(input('Quanto você deseja sacar: '))
n50 = 0
n20 = 0
n10 = 0
n1 = 0
while True:
    if sac - 50 > -1:
        n50 += 1
        sac -= 50
    elif sac - 20 > -1:
        n20 += 1
        sac -= 20
    elif sac - 10 > -1:
        n10 += 1
        sac -= 10
    else:
        n1 += 1
        sac -= 1
    if sac == 0:
        break
print(f'Notas de R$50,00: {n50}')
print(f'Notas de R$20,00: {n20}')
print(f'Notas de R$10,00: {n10}')
print(f'Notas de R$1,00: {n1}')