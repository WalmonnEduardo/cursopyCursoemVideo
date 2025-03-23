nome = str(input('Nome: ')).strip()
media = float(input('Média: '))
if media < 6:
    situacao = 'recuperação'
elif media < 8:
    situacao = 'tranquilo'
else:
    situacao = 'excelência'
aluno = {
    'nome':nome,
    'media':media,
    'situacao':situacao
}
for k,v in aluno.items():
    print(f'{k} = {v}')