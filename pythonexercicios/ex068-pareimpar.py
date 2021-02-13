from random import randint

while True:
    print('-='*30)
    print(f'VAMOS JOGAR PAR E IMPAR')
    print('-='*30)

    vitjogador = 0
    while True:
        opcaojogador = ' '
        jogador = int(input('Digite um valor: '))
        while opcaojogador not in 'PI':
            opcaojogador = input('Você escolhe Par ou Impar? [P/I] ').strip().upper()[0]
        print('-'*60)
        computador = randint(0, 10)
        soma = jogador + computador
        if soma % 2 == 0:
            print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {soma} e DEU PAR.')
            print('-'*60)
            if opcaojogador == 'P':
                print(f'Você VENCEU...\nVamos mais 1....')
                vitjogador += 1
                print('-' * 60)
                print()
            else:
                print(f'Computador VENCEU.')
                break
        else:
            print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {soma} e deu IMPAR.')
            print('-'*60)
            if opcaojogador == 'I':
                print(f'Você VENCEU.... \nVamos mais 1....')
                vitjogador += 1
                print('-' * 60)
                print()
            else:
                print(f'Computador VENCEU.')
                break

    print('-='*30)
    print(f'GAME OVER! Você venceu {vitjogador} partidas.')
    r = input(f'QUER JOGAR NOVAMENTE? [S/N]').strip().upper()[0]
    if r == 'N':
        break
