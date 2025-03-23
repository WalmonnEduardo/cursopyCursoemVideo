def notas(*notas,sit=False):
    """A função notas recebe quantos parâmetros você queira e retorna um dicionário com a quantidade de notas, maior nota, menor nota, média das notas e situação opicional
    notas(*notas,sit=True)"""
    maxi = max(notas)
    mini = min(notas)
    quant = len(notas)
    media = sum(notas) / len(notas)
    if media < 6 and sit:
        situ = 'Ruim'
    elif media < 7:
        situ = 'Razoável'
    else:
        situ = 'Boa'
    if sit:
        return {
            'Quantidade':quant,
            'Máxima':maxi,
            'Mínima':mini,
            'Média':media,
            'Situação':situ
        }
    else:
        return {
            'Quantidade':quant,
            'Máxima':maxi,
            'Mínima':mini,
            'Média':media,
        }
r = notas(10,9,8,7,6,5,4,3,2,1,sit=True)
for k,v in r.items():
    print(f'{k}: {v}')
help(notas)