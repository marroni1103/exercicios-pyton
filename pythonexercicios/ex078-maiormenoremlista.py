numeros = []
for v in range(0, 5):
    numeros.append(int(input(f'Digite um valor para a posiçao {v}: ')))
print('-='*20)
print(f'Você digitou os nuemros: {numeros}')

print(f'O maior numerido digitado foi {max(numeros)} nas posições ', end='')
for c, v in enumerate(numeros):
    if v == max(numeros):
        print(f'{c}...', end='')

print(f'\nO menor numero digitado foi {min(numeros)} nas posições ', end='')
for c, v in enumerate(numeros):
    if v == min(numeros):
        print(f'{c}...', end='')
