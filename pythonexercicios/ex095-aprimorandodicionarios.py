listajogadores = []
jogador = {}
while True:
    jogador.clear()
    jogador = {'nome': input('Nome do Jogador: ')}
    listgols = []
    cont = 0
    qtdpart = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    while cont < qtdpart:
        gols = int(input(f'Quantos gols marcados na partida {cont+1}? '))
        listgols.append(gols)
        cont += 1
    jogador['gols'] = listgols.copy()
    jogador['total'] = sum(listgols)
    listajogadores.append(jogador.copy())
    listgols.clear()
    while True:
        r = input('Quer continuar? [S/N] ').strip().upper()[0]
        if r in 'SN':
            break
        print(f'Erro. Tente novanmente.')
    if r == 'N':
        break

print('-='*20)
print(listajogadores)
print('-='*20)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(listajogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*20)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para o programa) '))
    if busca == 999:
        print(f'*** PROGRAMA ENCERRADO ***')
        break
    if busca >= len(listajogadores):
        print('Erro. Não existe jogador cadastrado com esse codigo.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {listajogadores[busca]["nome"]}:')
        for i, g in enumerate(listajogadores[busca]["gols"]):
            print(f' -> No jogo {i+1} fez {g} gols.')
    print('-'*40)





