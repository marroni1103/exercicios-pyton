print('GERADOR DE PA!')
print('-='*10)
inicio = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
cont = 1
soma = inicio

while cont <= 10:
    print(soma, end=' ')
    soma = soma + razao
    cont += 1
print('-> FIM')
