d = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km foi andando? '))
print('O total a pagar é R${:.2f}'.format(60*d+0.15*km))