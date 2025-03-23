nomec = str(input('Digite seu nome completo: ')).strip()
nomemax = nomec.upper()
nomemin = nomec.lower()
nome1 = nomec.split()
nome1 = nome1[0]
l1 = len(nome1)
nomeat = nomec.replace(' ','')
nomeclen = len(nomeat)
print('Analisando seu nome...')
print("""
        Seu nome em letras maiúsculas é {0}
        Seu nome em letras minúsculas é {1}
        A quantidade de letras no seu nome é {2}
        O seu primeiro nome é {3} e tem {4} letras.
        """.format(nomemax,nomemin,nomeclen,nome1,l1))