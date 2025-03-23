num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
um = num // 1000 % 10
print("""Analisando o número {0}
Unidade: {1}
Dezena: {2}
Centena: {3}
Unidade de milhar: {4}""".format(num,u,d,c,um))