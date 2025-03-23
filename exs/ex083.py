e = str(input('Digite uma expressão para validar: '))
a = 0
f = 0
for l in e:
    if l == '(':
        a += 1
    if l == ')':
        f += 1
if a == f:
    print('A expressão é válida!')
else:
    print('A expressão é inválida!')