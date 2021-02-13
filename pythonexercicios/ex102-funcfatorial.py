def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um numero
    :param num: numero a ser calculado
    :param show:(opcional) Mostrar a conta ou nao
    :return: O valor fatorial de um numero num
    """
    f = 1
    print('-'*30)
    if show:
        for c in range(num, 0, -1):
            if c > 1:
                print(f'{c} X ', end='')
            else:
                print(f'{c}', end=' ')
            f *= c
        print(f'= {f}')
    else:
        for c in range(num, 1, -1):
            f *= c
        print(f)


fatorial(5)
fatorial(5, True)
help(fatorial)
