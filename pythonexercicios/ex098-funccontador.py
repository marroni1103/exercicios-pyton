from time import sleep


def contador(i, f, p):
    if i < f:
        print(f'Contagem de {i} a {f} de {p} em {p}: ')
        for n in range(i, f+1, p):
            print(n, end=' ')
            sleep(0.3)
        print('FIM')
    else:
        if p > 0:
            print(f'Contagem de {i} a {f} de {p} em {p}:')
        elif p == 0:
            print(f'Contagem de {i} a {f} de 1 em 1:')
        else:
            print(f'Contagem de {i} a {f} de {-p} em {-p}:')
        if p > 0:
            for n in range(i, f-1, -p):
                print(n, end=' ')
                sleep(0.3)
            print('Fim')
        elif p == 0:
            for n in range(i, f-1, -1):
                print(n, end=' ')
                sleep(0.3)
            print('Fim')
        else:
            for n in range(i, f-1, p):
                print(n, end=' ')
                sleep(0.3)
            print('Fim')
    sleep(1)
    print('-=' * 20)


print('-=' * 20)
contador(1, 10, 1)
contador(10, 0, 2)
print(f'Agora é sua vez de personalizar a contagem.')
i = int(input('Inicio: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))
print('-=' * 20)
contador(i, f, p)
