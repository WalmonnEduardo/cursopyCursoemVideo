n = int(input('Digite um número para fazer o seu fatorial: '))
r = 1
print('{0}! = '.format(n),end='')
while n > 0:
    r *= n
    print('{0} x '.format(n),end='') if n != 1 else print('{0} = {1}'.format(n,r))
    n -= 1