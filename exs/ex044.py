preco = float(input('Digite o valor da vompra: R$'))
print('''{:=^40}
Formas de pagamento:
====================================
[ 1 -> A vista dinheiro/cheque     ]
====================================
[ 2 -> A vista cartão              ]
====================================
[ 3 -> 2x cartão                   ]
====================================
[ 4 -> 3x ou mais cartão           ]
====================================
'''.format(' LOJAS GUANABARA '))
esc = int(input('Escolha: '))
if esc == 1:
    t = preco - preco*0.1
elif esc == 2:
    t = preco - preco*0.05
elif esc == 3:
    t = preco
    par = t/2
    print('Sua compra será parcelada em 2 vezes de R${:.2f} sem juros'.format(par))
elif esc == 4:
    t = preco + preco*0.2
    tp = int(input('Quantas parcelas: '))
    par = t/tp
    print('Sua compra será parcelada em {0} vezes de R${1:.2f} com juros'.format(tp,par))
else:
    t = preco
    print('Opição inválida de pagamento')
print('Sua compra de R${0:.2f} vai dar R${1:.2f} no final'.format(preco,t))