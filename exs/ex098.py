def l():
    print('-'*60)

def contar(*nums):
    nuns = list()
    for n in nums:
        nuns.append(n)
    if len(nuns) < 2 and len(nuns) > 3:
        print('Você não quer contar nada')
    elif len(nuns) == 2:
        if nuns[0] > nuns[1]:
            for i in range(nuns[0],nuns[1],-1):
                print(i,end=' -> ')
        else:
            for i in range(nuns[0],(nuns[1]+1)):
                print(i,end=' -> ')
    else:
        p = nuns[2]
        if nuns[0] > nuns[1]:
            if nuns[2] > 0:
                p -= nuns[2]*2
            for i in range(nuns[0],(nuns[1]-1),p):
                print(i,end=' -> ')
        else:
            if nuns[2] < 0:
                p -= nuns[2]*2
            for i in range(nuns[0],(nuns[1]+1),p):
                print(i,end=' -> ')
    print('FIM')

l()
contar(1,10)
l()
contar(10,0)
l()
i = int(input('Digite o valor de inicio: '))
f = int(input('Digite o valor de fim: '))
p = int(input('Digite o valor de progreção: '))
if p == 0:
    contar(i,f)
else:
    contar(i,f,p)
l()