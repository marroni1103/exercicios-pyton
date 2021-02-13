alunos = []
aluno = ' '
while aluno != 'Sair':
    aluno = input('Informe o nome do aluno ou Sair para sair do programa: ').title()
    alunos.append(aluno)

del alunos[-1]

alunos.sort()
print(f'A ordem de apresentação do trabalho será {alunos}')
