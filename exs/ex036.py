c = float(input('Valor da casa: '))
s = float(input('Salário: '))
anos = int(input('Em quantos anos: '))
prest = c / (anos*12)
print('Para comprar a casa de R${0:.2f} em {1} a prestação será R${2:.2f} por mês'.format(c,anos,prest))

if prest > (s*0.3):
    print('Empréstimo não aprovado!')
else:
    print('Empréstimo aprovado!')