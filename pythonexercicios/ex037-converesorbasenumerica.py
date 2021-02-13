n1 = int(input('Informe um numero inteiro: '))
print('Opções de conversões: ')
print('1 - Converter em Binario')
print('2 - Converter em Octal')
print('3 - Converter em Hexadecimal')
escolha = int(input('Qual sua escolha? '))
if escolha == 1:
    print(f'{n1} convertido para binario é igual a {bin(n1)[2:]}')
elif escolha == 2:
    print(f'{n1} convertido em Octal é {oct(n1)[2:]}')
elif escolha == 3:
    print(f'{n1} convertido para Hexadecimal é {hex(n1)[2:]}')
else:
    print('Opção invalida. Tente novamente.')