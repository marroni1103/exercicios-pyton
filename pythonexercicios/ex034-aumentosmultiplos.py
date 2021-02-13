salario = float(input('Informe o salario do funcionario: R$ '))
if salario >= 1250:
    novosalario = salario + (salario * 10 / 100)
    print(f'O novo salario com o aumento de 10% é de R$ {novosalario:.2f}.')
else:
    novosalario = salario + (salario * 15 / 100)
    print(f'O novo salario com o aumento de 15% é de R$ {novosalario:.2f}.')
