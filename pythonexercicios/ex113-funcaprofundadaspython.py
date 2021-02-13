def leiaint(txt):
    while True:
        try:
            num = int(input(f'{txt}'))
            break
        except:
            print(f'\033[31mErro. Digite um numero inteiro valido\033[m')
    return num


def leiareal(txt):
    while True:
        try:
            num = float(input(f'{txt}'))
            break
        except:
            print(f'\033[31mErro. Digite um numero real valido\033[m')
    return num


inteiro = leiaint('Digite um numero inteiro: ')
real = leiareal('Digite um numero real: ')
print(f'O numero inteiro digitado foi {inteiro} e o real foi {real}.')
