from time import sleep
from random import randint


def sortear():
    numeros = []
    for n in range(0, 5):
        n = randint(1, 10)
        numeros.append(n)
    return numeros


def somapar(numeros):
    print(f'Sorteando 5 valores da lista: ', end=' ')
    for num in numeros:
        print(num, end=' ')
        sleep(0.5)
    print('PRONTO!!')
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    print(f'A soma dos pares dos numeros sorteados {numeros}, temos {soma}')


somapar(sortear())
