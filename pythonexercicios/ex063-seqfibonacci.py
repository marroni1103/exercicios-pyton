num = int(input('Informe quantos numeros quer ver da sequencia Fibonacci: '))
n1 = 0
n2 = 1
cont = 1
soma = 0
while cont <= num:
    print(soma, end=' ')
    n1 = n2
    n2 = soma
    soma = n1 + n2
    cont += 1
print('FIM')
print(f'Obrigado por usar o programa.')