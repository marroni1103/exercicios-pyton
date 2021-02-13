from random import randint
from time import sleep
while True:
    npensado = randint(0, 10)

    palpites = 1

    print('-='*22)
    print('Pensei em um numero entre 0 e 10...')
    print('-='*22)
    numero = int(input('Tente adivinhar qual é: '))
    print('PROCESSANDO.....')
    sleep(1)
    while numero != npensado:
        if numero > npensado:
            print('hahah... não não.. é menos... tente de novo.')
            numero = int(input('Qual acha que é? '))
            palpites += 1
        else:
            print('hahah... não não..é mais.... tente de novo.')
            numero = int(input('Qual acha que é? '))
            palpites += 1

    print(f'Parabens... vc acertou.. tinha pensado no {npensado}.')
    print(f'Você precisou de {palpites} chances para acertar.')
    r = input(f'QUER JOGAR NOVAMENTE? [S/N] ').strip().upper()[0]
    if r == 'N':
        break