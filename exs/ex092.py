from datetime import date
dados = dict()
dados['nome'] = str(input('Nome: ')).strip()
nasc = int(input('Ano de nascimento: '))
dados['idade'] = date.today().year - nasc
dados['ctps'] = int(input('Carteira de trabalho[Não tem = 0]: '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: '))
    dados['aposentadoria'] = dados['idade'] + (( dados['contratacao'] + 35 ) - date.today().year)
for k,v in dados.items():
    print(f'{k} = {v}')