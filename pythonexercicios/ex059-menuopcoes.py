from time import sleep
n1 = int(input('Informe o primeiro numero: '))
n2 = int(input('Informe o segundo numero: '))
opcao = 0
while opcao != 5:
    print("""Escolha uma das opções abaixo:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos numeros
    [5] Sair do programa
    """)
    opcao = int(input('>>>> Qual opção desejada? '))
    if opcao == 1:
        print(f'A soma entre {n1} + {n2} é {n1 + n2}')
    elif opcao == 2:
        print(f'O produto entre {n1} x {n2} é {n1 * n2}')
    elif opcao == 3:
        if n1 > n2:
            print(f'O maior numero digitado foi {n1}')
        elif n1 < n2:
            print(f'O maior numero digitado foi {n2}')
        else:
            print(f'Não existe maior, os 2 são iguais')
    elif opcao == 4:
        print('Informe os numeros novamente.')
        n1 = int(input('\nInforme o primeiro numero: '))
        n2 = int(input('Informe o segundo numero: '))
    elif opcao == 5:
        print(f'Finalizando...')
        sleep(1)
        print(f'Obrigado por usar o sistema. Até a próxima.')
    else:
        print('Opção invalida!')
    print('-=' * 20)
    sleep(2)
