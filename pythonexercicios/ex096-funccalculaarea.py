def area(l, c):
    print(f'A área do terreno de {l} x {c} é de {l * c}m²')


print('-'*30)
print('      Controle de terreno   ')
print('-'*30)
l = float(input('Largura (m): '))
c = float(input('Comprimento: '))
area(l, c)
