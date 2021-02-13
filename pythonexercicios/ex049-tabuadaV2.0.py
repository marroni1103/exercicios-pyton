numero = int(input('Informe o numero para saber sua tabuada: '))
print('-'*12)
for c in range(0, 11):
    print(f'{numero} X {c:2} = {numero*c}')
print('-'*12)