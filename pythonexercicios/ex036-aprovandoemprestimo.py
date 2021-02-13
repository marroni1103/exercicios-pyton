casa = float(input('Informe o valor do imóvel: R$ '))
salario = float(input('Informe o salario do comprador: R$ '))
anos = float(input('Informe em quantos anos quer pagar: '))

prestacao = casa / (anos * 12)

if prestacao > (salario * 30 / 100):
    print(f'Infelizmente prestação maior que 30% do salario!')
    print(f'\033[31mEMPRESTIMO NEGADO.\033[m')
    print( f'Sua prestação seria de R${prestacao:.2f}' )
else:
    print('\033[32mEMPRESTIMO APROVADO!!\033[m')
    print( f'Sua prestação será de R${prestacao:.2f}' )
