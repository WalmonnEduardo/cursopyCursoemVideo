from ex107110 import moeda
p = float(input('Digite o preço: R$'))
print(f'A metade é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro é {moeda.moeda(moeda.dobro(p))}')
print(f'O aumento 10% é {moeda.moeda(moeda.aumentar(p,10))}')
print(f'A diminuição 10% é {moeda.moeda(moeda.diminuir(p,10))}')