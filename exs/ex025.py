nomec = str(input('Digite seu nome completo: ')).strip()
nome = nomec.upper()
r = 'SILVA' in nome
print("""Analisando nome {0}...
Tem Silva no nome: {1}""".format(nomec,r))