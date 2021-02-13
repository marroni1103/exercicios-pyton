def leiaDinheiro(msn):
    valido = False
    while not valido:
        entrada = str(input(msn)).strip().replace(',', '.')
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mErro. Digite um preço valido\033[m')
        else:
            valido = True
            return float(entrada)


