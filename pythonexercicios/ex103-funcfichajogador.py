def ficha(nome, gols):
    if nome == '':
        nome = '<desconhecido>'
    if gols.isnumeric():
        gols = int(g)
    else:
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


n = input('Nome do jogador: ').strip().title()
g = input('Numero de gols: ').strip()
ficha(n, g)
