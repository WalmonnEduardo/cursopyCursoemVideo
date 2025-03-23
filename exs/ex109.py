from ex107110 import moeda
p = float(input('Digite o preço: R$'))
print(f'A metade é {moeda.metade(p,True)}')
print(f'O dobro é {moeda.dobro(p,True)}')
print(f'O aumento 10% é {moeda.aumentar(p,10,True)}')
print(f'A diminuição 10% é {moeda.diminuir(p,10,True)}')