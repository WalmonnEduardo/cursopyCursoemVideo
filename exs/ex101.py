def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        m = 'Você ainda não pode votar, VOTO NEGADO'
    elif idade < 18 or idade > 65:
        m = 'Você pode votar mas não é necessário, VOTO OPICIONAL'
    else:
        m = 'Você deve votar, VOTO OBRIGATÓRIO'
    return m
print(voto(int(input('Qual é seu ano de nascimento: '))))