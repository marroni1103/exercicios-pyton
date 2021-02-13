print('{:=^40}'.format(' Lojas Pereira '))

produto = float(input('Valor final das compras: R$ '))
print('''Opções de pagamento:
1 - A vista em dinheiro ou cheque
2 - A vista em cartão
3 - Em até 2x no cartão
4 - 3x ou mais no cartão''')
opcao = int(input('Qual opção desejada? '))

if opcao == 1:
    print(f'Pagando dessas forma você ganha 10% de desconto.')
    print(f'Novo valor do produto é de R$ {produto - (produto * 10 / 100):.2f}')
elif opcao == 2:
    print('Pagando dessa forma você ganha 5% de desconto.')
    print(f'Novo valor do produto é de R$ {produto - (produto * 5 / 100):.2f}')
elif opcao == 3:
    print(f'Para essa opção não temos como dar desconto.')
    print(f'O valor do produto se mantem em R${produto:.2f}')
    print(f'Sua compra será parcelada em 2x de R$ {produto / 2:.2f}.')
elif opcao == 4:
    parcelas = int(input('Informe a quantidade de parcelas: (3 até 10) '))
    print(f'Para essa opção temos um acrescimo de 20% de juros.')
    print(f'Novo valor do produto é de {produto + (produto * 20 / 100):.2f}')
    print(f'Sua parcela será de R$ {((produto + (produto * 20 / 100))/parcelas):.2f}')
else:
    print(f'\033[31mOpção invalida de pagamento.\033[m')
