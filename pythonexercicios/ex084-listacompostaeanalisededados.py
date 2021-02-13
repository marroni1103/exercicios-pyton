galera = []
dados = []
menorpeso = maiorpeso = 0
while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))
    if len(galera) == 0:
        maiorpeso = menorpeso = dados[1]
    else:
        if dados[1] > maiorpeso:
            maiorpeso = dados[1]
        if dados[1] < menorpeso:
            menorpeso = dados[1]
    galera.append(dados[:])
    dados.clear()
    r = ' '
    while r not in 'NnSs':
        r = input('Deseja continuar? [S/N] ').strip().lower()[0]
    if r == 'n':
        break


print('=-'*30)
print(f'Ao todo você cadastrou {len(galera)} pessoas.')
print(f'O menor peso foi de {menorpeso}Kg. Peso de ', end='')
for p in galera:
    if p[1] == menorpeso:
        print(f'[{p[0]}]', end=' ')
print(f'\nO maior peso foi de {maiorpeso}Kg. Peso de ', end='')
for p in galera:
    if p[1] == maiorpeso:
        print(f'[{p[0]}]', end='')
