print('''------------------------------
Sequencia de Fibonacci
------------------------------
''')
q = int(input('Quantos termos você quer mostrar: '))
i = 1
n = 0
a = 1
print(n,end=' -> ')
while i < q:
    p = n+a
    a = n 
    n = p
    print(n,end=' -> ')
    i += 1
print('Fim')