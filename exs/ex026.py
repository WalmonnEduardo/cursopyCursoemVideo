frase = str(input('Digite uma frase: ')).strip()
frasem = frase.upper()
print("""Analisando frase '{0}'
Tem {1} vezes a letra A
A letra A aparece pela primeira vez na posição {2}
A letra A aparece pela ultima vez na posição {3}
""".format(frase,frasem.count('A'),frasem.find('A')+1,frasem.rfind('A')))