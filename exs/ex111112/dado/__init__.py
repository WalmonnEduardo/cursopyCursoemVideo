def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').replace(' ','').strip()
        if entrada.isalpha() or entrada == '':
            print(f'ERRO, "{entrada}" é inválida')
        else:
            valido = True
            return float(entrada)