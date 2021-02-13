soma = cont = 0
valormaisbarato = cont1 = 0
nomemaisbarato = ' '
print(f'-'*20)
print('{:-^20}'. format(' LOJAS GUSTAVO '))
print(f'-'*20)
while True:
    nomeproduto = input(f'Nome do produto: ').strip().title()
    preco = float(input(f'Preço: R$ '))
    cont1 += 1
    soma += preco
    if preco > 1000:
        cont += 1
    if cont1 == 1 or preco < valormaisbarato:
        valormaisbarato = preco
        nomemaisbarato = nomeproduto
    continuar = ' '
    while continuar not in 'NS':
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break
print('-='*20)
print('FIM DO PROGRAMA')
print('-='*20)
print(f"""
O total da compra foi de R${soma:.2f}
Temos {cont} produtos acima dos R$ 1000,00
O produto mais barato foi {nomemaisbarato} que custa R${valormaisbarato:.2f}.""")
