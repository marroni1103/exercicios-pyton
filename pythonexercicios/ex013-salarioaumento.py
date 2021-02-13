salario = float(input('Informe o salario atual: R$ '))
aumento = float(input('Informe o valor do aumento (sem o sinal de %): '))

print(f'O novo salario com o aumento de \033[33m{aumento}%\033[m é de \033[32mR$ {salario+(salario*aumento/100):.2f}\033[m')