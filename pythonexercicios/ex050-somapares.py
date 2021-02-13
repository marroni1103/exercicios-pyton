soma = 0
for n in range(1, 7):
    num = int(input(f'Informe o {n}° valor: '))
    if num % 2 == 0:
        soma += num

print(f'A soma dos numeros pares digitado é de {soma}.')
