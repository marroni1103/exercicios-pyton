sair = ' '
lista = []
cont = 0
while sair != 'n':
    n = int(input('Digite um numero: '))
    lista.append(n)
    cont += 1
    sair = input('Deseja sair? [S/N]').strip().lower()[0]

print(f'Voce digitou {cont} numeros.')
print(f'A media dos numeros digitados é {sum(lista) / cont}')
print(f'O maior numero digitado foi {max(lista)}')
print(f'O menor numero digitado foi {min(lista)}')
