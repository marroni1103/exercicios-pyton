produtos = ('Pão', 1,
            'Manteiga', 2,
            'Café', 1.9,
            'Cerveja', 3.5,
            'Refrigerante', 2.5,
            'Chocolate', 4.87,
            'Caneta', 2,
            'Lapis', 1.5,
            'Livros', 25.5,
            'Micro-Ondas', 452)


print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for pos in range(len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R$ {produtos[pos]:>7.2f}')
