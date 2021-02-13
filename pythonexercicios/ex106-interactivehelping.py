def ajuda():
    from time import sleep
    while True:
        tam1 = len('SISTEMA DE AJUDA PyHELP') + 4
        print('\033[42m~'*tam1)
        print('  SISTEMA DE AJUDA PyHELP')
        print(f'~'*tam1)
        opcao = input('\033[mFunção ou Biblioteca > ')
        if opcao == 'fim':
            tam2 = len('ATÉ LOGO!') + 4
            sleep(1)
            print('\033[45m~'*tam2)
            print(f'  ATÉ LOGO!')
            print(f'~'*tam2)
            break
        else:
            tam3 = len(f"Acessando o manual do '{opcao}'") + 4
            print('\033[44m~' * tam3)
            print(f"  Acessando o manual do '{opcao}'")
            print(f'~' * tam3)
            sleep(1)
            print(f'\033[7;30m', end='')
            help(opcao)
            print(f'\033[m', end='')
            sleep(1)


ajuda()
