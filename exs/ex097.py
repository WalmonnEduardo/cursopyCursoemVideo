def titulo(txt):
    n = len(txt) + 5
    print('-'*n)
    print(f'{txt:^{n}}')
    print('-'*n)
titulo('Curso em Vídeo')
titulo('Aula 20')
titulo('Função')