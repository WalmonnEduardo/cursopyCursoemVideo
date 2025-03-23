def aumentar(preco,taxa,form=False):
    res = preco + (preco * taxa / 100)
    if form:
        res = moeda(res)
    return res


def diminuir(preco,taxa,form=False):
    res = preco - (preco * taxa / 100)
    if form:
        res = moeda(res)
    return res


def dobro(preco,form=False):
    res = preco * 2
    if form:
        res = moeda(res)
    return res


def metade(preco,form=False):
    res = preco / 2
    if form:
        res = moeda(res)
    return res

def moeda(preco,moeda='R$',form=False):
    moeda = f'{moeda}{preco:.2f}'.replace('.',',')
    if form:
        res = moeda(res)
    return moeda


def resumo(p,a=10,r=10):
    print(f'A metade é {metade(p,True)}')
    print(f'O dobro é {dobro(p,True)}')
    print(f'O aumento {a}% é {aumentar(p,a,True)}')
    print(f'A diminuição {r}% é {diminuir(p,r,True)}')