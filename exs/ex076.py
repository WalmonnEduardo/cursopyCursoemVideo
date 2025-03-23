list = ('Lápis',3.5,'Caderno',50.0,'Mochila',400.0,'livro',34.90)
print('-'*50)
print(f'{' Lista de Preços ':^50}')
print('-'*50)
for i in range(len(list)):
    if i % 2 == 0:
        print(f'{list[i]:.<30}',end='')
    else:
        print(f' R${list[i]:>7.2f}')