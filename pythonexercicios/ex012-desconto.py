preco = float(input('Informe o preço do produto: R$ '))
desconto = float(input('Informe o desconto (sem o sinal de %): '))

print(f'O novo preço com o desconto informado é de R$ {preco - (preco*desconto/100):.2f}')