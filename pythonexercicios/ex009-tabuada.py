numero = int(input('Informe o numero para saber sua tabuada: '))
cont = 1
print('-'*12)
while cont <= 10:
    print(f'{numero} X {cont:2} = {numero*cont}')
    cont += 1
print('-'*12)