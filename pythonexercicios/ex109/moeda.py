def metade(valor=0, formato=False):
    res = valor / 2
    return res if formato is False else moeda(res)


def dobro(valor=0, formato=False):
    res = valor * 2
    return res if formato is False else moeda(res)


def aumentar(valor=0, taxa=0, formato=False):
    res = valor + (valor * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(valor=0, taxa=0, formato=False):
    res = valor - (valor * taxa / 100)
    return res if formato is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')

