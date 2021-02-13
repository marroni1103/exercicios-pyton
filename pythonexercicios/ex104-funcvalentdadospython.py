def leiaint(txt):
    while True:
        num = str(input(f'{txt}'))
        if num.isnumeric():
            num = int(num)
            break
        else:
            print(f'\033[31mErro. Digite um numero inteiro valido\033[m')
    return num


n = leiaint('Digite um numero: ')
print(f'Você acabou de digitar o numero {n}')
