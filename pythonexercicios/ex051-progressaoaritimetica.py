inicio = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))

lista = []

fim = inicio + (10-1)*razao

for n in range(inicio, fim+razao, razao):
    lista.append(n)


print(f'Os 10 primeiros numeros dessa progressão aritmética é {lista}')