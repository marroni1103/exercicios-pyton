lista = []
listapar = []
listaimpar = []

while True:
    lista.append(int(input('Digite um numero: ')))
    resp = ' '
    while resp not in 'NnSs':
        resp = input('Deseja continuar? [S/N] ').strip().lower()[0]
    if resp == 'n':
        break

for v in lista:
    if v % 2 == 0:
        listapar.append(v)
    else:
        listaimpar.append(v)


print('-='*20)
print(f'A lista completa de numeros é {lista}.')
print(f'A lista de numeros pares é {listapar}.')
print(f'A lista de numeros impares é {listaimpar}.')
