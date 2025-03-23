n = int(input('Digite um número: '))
print(20*'=')
for i in range(1,11):
    print('{0} x {1:>2} = {2}'.format(n,i,(n*i)))
print(20*'=')