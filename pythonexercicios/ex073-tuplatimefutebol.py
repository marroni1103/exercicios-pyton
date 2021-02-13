times = ('Internacional', 'Flamengo', 'Atletico-MG', 'São Paulo', 'Fluminense', 'Palmeiras', 'Grêmio',
         'Corinthians', 'RB Bragantino', 'Santos', 'Athletico-PR', 'Ceará', 'Atletico-GO', 'Vasco',
         'Bahia', 'Sport', 'Fortaleza', 'Goiás', 'Coritiba', 'Botafogo')

print('-=' * 20)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 20)
print(f'Os cinco primeiros colocados são {times[:5]}')
print('-=' * 20)
print(f'Os ultimos 4 colocados são {times[-4:]}')
print('-=' * 20)
print(f'Lista em ordem alfabetica {sorted(times)}')
print('-=' * 20)
print(f'Em 04/02/2021 o Palmeiras está na {times.index("Palmeiras") + 1}º posição')
