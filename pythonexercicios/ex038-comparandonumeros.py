n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))

print(f'Os numeros informados foram {n1} e {n2}')
if n1 > n2:
    print('O primeiro numero é maior que o segundo')
elif n1 < n2:
    print('O segundo numero é maior que o primeiro')
else:
    print('Não existe valor maior. Ambos são iguais.')
