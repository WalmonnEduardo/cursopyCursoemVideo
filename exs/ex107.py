from ex107110 import moeda
p = float(input('Digite o preço: R$'))
print(f'A metade é R${moeda.metade(p)}')
print(f'O dobro é R${moeda.dobro(p)}')
print(f'O aumento 10% é R${moeda.aumentar(p,10)}')
print(f'A diminuição 10% é R${moeda.diminuir(p,10)}')