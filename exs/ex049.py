n = int(input('Digite um número para vermos a tabuada: '))
for i in range(1,11):
    print("{0} x {1:>2} = {2}".format(n,i,n*i))