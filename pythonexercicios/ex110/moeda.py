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


def resumo(p=0, tx1=10, tx2=5):
    print('-'*30)
    print(f'RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço Analisado: \t{moeda(p)}')
    print(f'Dobro do Preço: \t{dobro(p, True)}')
    print(f'Metade do valor: \t{metade(p, True)}')
    print(f'{tx1}% de aumento: \t{aumentar(p, tx1, True)}')
    print(f'{tx2}% de redução: \t{diminuir(p, tx2, True)}')
    print('-'*30)



