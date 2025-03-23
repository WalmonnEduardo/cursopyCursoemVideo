f = str(input('Digite uma frase: ')).strip().upper()
f = f.replace(' ','')
rf = ''
t = f[::-1]
for l in range(len(f)-1,-1,-1):
    rf += f[l]
if rf == f:
    print('A frase {0} é um palíndromo porque seu oposto é {1}'.format(f,rf))
else:
    print('A frase {0} não é um palíndromo porque seu oposto é {1}'.format(f,rf))
#print(t)