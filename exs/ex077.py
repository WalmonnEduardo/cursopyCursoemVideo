palavras = ('aprender','programar','linguagem','python','curso','gratis','estudar','praticar','trabalhar','mercardo','programador','futuro')
for p in palavras:
    print(f'Na palavra {p.upper()} temos as vogais ',end='')
    for l in p:
        if l in 'aeiou':
            print(l,end=' ')
    print()