from random import choice

alunos = []
aluno = ''
while aluno != 'Sair':
    aluno = input('Informe o nome dos alunos para participarem do sorteio ou "sair" para sair: ').title()
    alunos.append(aluno)

del alunos[-1]

print(f'\033[36mO aluno sorteado para apagar o quadro foi {choice( alunos )}\033[m')
