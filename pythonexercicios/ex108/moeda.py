def metade(valor=0):
    res = valor / 2
    return res


def dobro(valor=0):
    res = valor * 2
    return res


def aumentar(valor=0, taxa=0):
    res = valor + (valor * taxa / 100)
    return res


def diminuir(valor=0, taxa=0):
    res = valor - (valor * taxa / 100)
    return res


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')

