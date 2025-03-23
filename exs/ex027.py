nome = str(input('Digite seu nome: ')).strip()
nome = nome.split()
p = nome[0]
u = nome[len(nome)-1]

print("""Prazer em te conhecer
Seu primeiro nome é {0}
Seu último nome é {1}
""".format(p,u))