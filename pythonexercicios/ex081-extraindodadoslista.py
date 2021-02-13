lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = ' '
    while resp not in 'ns':
        resp = input('Deseja continuar? [S/N] ').strip().lower()[0]
    if resp in 'Nn':
        break

print('-='*20)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print(f'O numero 5 faz parte da lista.')
else:
    print(f'O numero 5 não faz parte da lista.')

