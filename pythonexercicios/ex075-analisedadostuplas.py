numeros = (int(input('Digite o primeiro numero: ')),
           int(input('Digite o segundo numero: ')),
           int(input('Digite o terceiro numero: ')),
           int(input('Digite o quarto numero: ')))

print(f'Você digitou os numeros:', end=' ')
for n in numeros:
    print(f'{n}', end=' ')

print(f'\nO valor 9 apareceu {numeros.count(9)} vezes.')

if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3) + 1}° posição pela primeira vez.')
else:
    print(f'O valor 3 não consta na lista de números informados.')

print(f'Os valores pares digitados foram:', end=' ')
for pares in numeros:
    if pares % 2 == 0:
        print(f'{pares}', end=' ')
