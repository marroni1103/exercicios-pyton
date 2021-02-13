from utilidades import *
from time import sleep
from arquivos import *

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    cabecalho('MENU PRINCIPAL')
    opcao = menu(['Ver Cadastros', 'Cadastrar pessoas', 'Sair do sistema'])
    if opcao == 1:
        lerArquivo(arq)
    elif opcao == 2:
        print( '-' * 40)
        print( f'NOVO CADASTRO'.center(40))
        print( '-' * 40)
        nome = str(input('Nome: ')).strip().title()
        idade = leiaint('Idade: ')
        cadastrarpessoas(arq, nome, idade)
    elif opcao == 3:
        sairsistema()
        break
    else:
        print(f'\033[31mOpção invalida. Escolha novamente.\033[m')


