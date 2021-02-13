from time import sleep


def maior(* num):
    soma = maior = 0
    print('-='*20)
    print('Analisasndo os valores passados...')
    for valor in num:
        print(valor, end=' ')
        if soma == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        sleep(0.5)
    for valor in num:
        soma += 1
    print(f'Foram informados {soma} valores ao todo.')
    print(f'O maior numero informado foi {maior}.')
    sleep(0.5)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
