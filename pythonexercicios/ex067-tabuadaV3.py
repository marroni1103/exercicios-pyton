while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print( '-' * 20 )
    if n <= 0:
        break
    for num in range(1, 11):
        print(f'{n} x {num:2} = {n * num}')
    print('-'*20)

print(f'PROGRAMA ENCERRADO. Obrigado por usar o sistema. Volte sempre.')
