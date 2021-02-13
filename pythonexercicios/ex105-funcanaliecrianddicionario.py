def notas(*n, sit=False):
    """
    -> Funcao para analisar notas e situação dos alunos
    :param n: uma ou mais notas dos alunos (Aceita quantos for necessario)
    :param sit: valor opcional, informa a situação do aluno baseado na media
    :return: dicionario com varias informações da turma
    """
    resumo = {'total': len(n), 'maior': max(n), 'menor': min(n), 'media': sum(n) / len(n)}
    if sit:
        if resumo['media'] < 5:
            resumo['situação'] = 'RUIM'
        elif 5 <= resumo['media'] < 7:
            resumo['situação'] = 'RAZOAVEL'
        elif resumo['media'] >= 7:
            resumo['situação'] = 'BOA'

    return resumo


resp = notas(5.5, 2.5, 8.5, sit=True)
print(resp)
help(notas)
