soma = 0
cont = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        soma += n
        cont += 1

print(f'A soma dos numeros impares multiplos de 3 entre 0 e 500 é {soma}. Foram somados {cont} numeros.')
