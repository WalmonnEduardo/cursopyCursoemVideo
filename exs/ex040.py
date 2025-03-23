n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('A sua média é {:.2f}'.format(m))
if m < 5:
    print('Reprovado')
elif m < 7:
    print('Recuperação')
else:
    print('Aprovado')