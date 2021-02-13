qtd = int(input('Informe a quantidade de notas informadas: '))
soma = 0
cont = 1
cont2 = 1
while cont <= qtd:
    nota = float(input(f'Informe a nota {cont2}/{qtd}: '))
    soma += nota
    cont2 = cont2 + 1
    cont += 1

print(f'A media do aluno foi de {soma/qtd:.2f}')
