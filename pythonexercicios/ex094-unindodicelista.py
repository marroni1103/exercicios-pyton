listageral = []
temp = {}
somaidade = 0
while True:
    temp.clear()
    temp['nome'] = input('Nome: ')
    while True:
        temp['sexo'] = input('Sexo: [M/F] ').strip().upper()[0]
        if temp['sexo'] in 'MF':
            break
        else:
            print(f'Erro. Informe o Sexo novamente.')
    temp['idade'] = int(input('Idade: '))
    somaidade += temp['idade']
    listageral.append(temp.copy())
    while True:
        r = input('Quer continuar? [S/N] ').strip().upper()[0]
        if r in 'SN':
            break
        print('Erro. Tente novamente')
    if r == 'N':
        break


mediaidade = somaidade / len(listageral)
print(listageral)
print('-='*30)
print(f'-> O grupo tem {len(listageral)} pessoas.')
print(f'-> A média de idade é de {mediaidade:.2f}.')
print(f'-> As mulheres cadastradas foram: ', end='')
for pessoa in listageral:
    if pessoa['sexo'] == 'F':
        print(pessoa['nome'], end=' ')
print(f'\n-> Lista de pessoas acima da média de idade: ')
for pessoa in listageral:
    if pessoa['idade'] >= mediaidade:
        print(' ', end='')
        for k, v in pessoa.items():
            print(f'{k}: {v}; ', end='')
        print()
print(f' **** ENCERRADO ****')
