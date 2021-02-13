numeros = []
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print(f'Numero adicionado com sucesso...')
    else:
        print(f'Numero duplicado. O mesmo não será adicionado...')
    resp = ' '
    while resp not in 'ns':
        resp = input('Desena continuar? [S/N} ').strip().lower()[0]
    if resp in 'Nn':
        break
numeros.sort()
print('-='*30)
print(f'Os numeros digitaros foram {numeros}')
