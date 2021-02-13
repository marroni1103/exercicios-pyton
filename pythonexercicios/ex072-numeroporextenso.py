numeros = 'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', \
          'doze', 'treze', 'catorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte'

while True:
    num = int(input('Informe um numero entre 0 e 20: '))
    if num >= 0 and num <= 20:
        print(f'Você digitou o numero {numeros[num]}.')
        resp = ' '
        resp = input( 'Quer continuar? [S/N] ' ).strip().upper()[0]
        if resp == 'N' :
            break
    else:
        print(f'Tente novamente!', end=' ')
print(f'Obrigado por usar o meu sistema.')


