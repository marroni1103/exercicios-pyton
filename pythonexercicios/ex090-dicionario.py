aluno = {'nome': input('Nome: ')}
aluno['media'] = float(input(f'Media do aluno {aluno["nome"]}: '))
print(f'-> O nome é igual {aluno["nome"]}')
print(f'-> Média igual a {aluno["media"]}')
if aluno['media'] > 7.0:
    print(f'-> Situação é igual a APROVADO')
else:
    print(f'-> Situação é igual a REPROVADO')
