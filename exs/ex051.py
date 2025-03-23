p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
f = p + ( 10 - 1 ) * r
print('A progressão aritimética fica')
for i in range(p,f+r,r): 
    print(i,end=' -> ')
print('Acabou')