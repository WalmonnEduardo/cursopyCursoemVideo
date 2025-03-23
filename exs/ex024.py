cidade = str(input('Digite a cidade que vc nasceu: ')).strip()
print('Possui Santo no nome: {}'.format(cidade[:5].lower() == 'santo'))