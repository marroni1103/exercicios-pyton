palavras = ('COMPUTADOR', 'TECLADO', 'MOUSE', 'TELA', 'GRATIS', 'CURSO', 'PYTHON')

for p in palavras:
    print(f'\nNa palavra {p} temos as vogais: ', end='')
    for v in p:
        if v in 'AEIOU':
            print(v.lower(), end=' ')
