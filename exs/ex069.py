print('='*50)
print(f'{' Cadastro de Pessoas ':^50}')
print('='*50)
m18 = 0
m20 = 0
M = 0
while True:
    idade = int(input('Qual é sua idade: '))
    while True:
        sexo = str(input('Qual é seu sexo[M/F]: ')).strip().upper()[0]
        if sexo in 'FM':
            break
    if idade > 17:
        m18 += 1
    if sexo == 'F' and idade < 20:
        m20 += 1
    if sexo == 'M':
        M += 1
    print('='*50)
    while True:
        esc = str(input('Deseja continuar[S/N]: ')).strip().upper()[0]
        if esc in 'SN':
            break
    if esc == 'N':
        break
    print('='*50)
print(f'Total de pessoas com mais de 18 anos {m18}, total de mulheres com menos de 20 anos {m20}, total de homens {M}')