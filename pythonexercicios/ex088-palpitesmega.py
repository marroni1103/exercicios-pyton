from random import randint
from time import sleep
print('-'*30)
print(f'{"JOGOS DA MEGA SENA":^30}')
print('-'*30)
jogos = int(input('Quantos jogos quer sortear? '))
print(f'-=-=-=-=-= SORTEANDO {jogos} JOGOS -=-=-=-=-=')

for j in range(1, jogos+1):
    lista = []
    for num in range(0, 6):
        while True:
            n = randint(1, 60)
            if n not in lista:
                lista.append(n)
                break
    lista.sort()
    print(f'Jogo {j}: {lista}')
    sleep(1)
    lista.clear()
print(f'-=-=-=-=-=- < BOA SORTE > =-=-=-=-=-=-=')
