def fatorial(n, show=False):
    """
    Essa função retorna o fatorial de um número que estará na variável n
    Também temos um parâmetro opicional chamado show define se vc vai mostrar a conta feita ou não
    """
    f = 1
    s = ''
    for i in range(n,0,-1):
        f *= i
        if show and i != 1:
            s += str(i) + ' x '
        elif show and i == 1:
            s += str(i) + ' = '
    s += str(f)
    return s 
print(fatorial(int(input('Digite um número para fazer o fatorial: ')),True))