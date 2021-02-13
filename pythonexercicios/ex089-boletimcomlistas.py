from time import sleep
ficha = []
media = 0
while True:
    nome = input('Nome: ').strip().title()
    nota1 = float(input(f'Nota 1: '))
    nota2 = float(input(f'Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    r = ' '
    while r not in 'NnSs':
        r = input('Deseja continuar? [S/N] ').strip().lower()[0]
    if r == 'n':
        break
print('-='*30)
print(f'{"cod":<4}{"Nome":<10}{"Média":>13}')
print('-'*30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>13}')
print('-'*30)
while True:
    cont = int(input(f'Mostrar notas de qual aluno? (999 interrompe) '))
    if cont == 999:
        print(f'FINALIZANDO...')
        sleep(1)
        break
    if cont <= len(ficha) - 1:
        print(f'As notas do aluno {ficha[cont][0]} foram {ficha[cont][1]}')
    print('-'*30)
print(f'***** Obrigado por usar o sistema. *****')
