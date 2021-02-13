jogador = {'nome': input('Nome do Jogador: ')}
listgols = []
cont = 0
qtdpart = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
while cont < qtdpart:
    gols = int(input(f'    Quantos gols marcados na partida {cont+1}? '))
    listgols.append(gols)
    cont += 1
jogador['gols'] = listgols.copy()
jogador['Total'] = sum(listgols)

print('-='*30)
print(jogador)
print('-='*30)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')

print('-='*30)
print(f'O jogador {jogador["nome"]} fez {qtdpart} partidas.')
contpart = 1
for g in listgols:
    print(f'  -> Na partida {contpart}, fez {g} gols.')
    contpart += 1
print(f'Foi um total de {sum(listgols)} gols.')

