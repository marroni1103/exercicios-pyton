from random import choice
from time import sleep

while True:
    print('-='*15)
    print(f'Bem Vindo ao Jogo de JOKENPÔ')
    print('-='*15)

    opcaojogador = input('Informe sua opção Pedra, Papel ou Tesousa? ').title()
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')

    listapc = ['Pedra', 'Papel', 'Tesousa']

    opcaopc = choice(listapc)

    if opcaopc == 'Pedra' and opcaojogador == 'Tesoura':
        print(f'Eu escolho....{opcaopc.upper()}')
        print(f'HAHAHAHA... Ganhei de você.')
    elif opcaopc == 'Papel' and opcaojogador == 'Pedra':
        print(f'Eu escolho....{opcaopc.upper()}')
        print(f'HAHAHAHA... Ganhei de você.')
    elif opcaopc == 'Tesoura' and opcaojogador == 'Papel':
        print(f'Eu escolho....{opcaopc.upper()}')
        print(f'HAHAHAHA... Ganhei de você.')
    elif opcaojogador == 'Pedra' and opcaopc == 'Tesoura':
        print(f'Eu escolho....{opcaopc.upper()}')
        print(f'Droga você ganhou!!!')
    elif opcaojogador == 'Papel' and opcaopc == 'Pedra':
        print(f'Eu escolho....{opcaopc.upper()}')
        print(f'Droga você ganhou!!!')
    elif opcaojogador == 'Tesoura' and opcaopc == 'Papel':
        print(f'Eu escolho....{opcaopc.upper()}')
        print(f'Droga você ganhou!!!')
    elif opcaopc == opcaojogador:
        print(f'Eu escolho....{opcaopc.upper()}')
        print('Ninguem ganhou. Vamos outra!!')
    else:
        print('Opção Invalida. Tente novamente.')

    r = input('DESEJA JOGAR MAIS 1? [S/N] ').strip().upper()[0]
    if r == 'N':
        break
