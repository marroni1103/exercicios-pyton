cont = soma = n = 0
while n != 999:
    n = int(input('Digite um numero ou 999 para sair: '))
    if n != 999:
        soma += n
        cont += 1

print(f'Você digitou {cont} numeros e a soma deles deu {soma}')
print(f'Obrigado por usar o sistema.')


