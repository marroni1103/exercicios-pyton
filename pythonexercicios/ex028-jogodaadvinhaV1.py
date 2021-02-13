from random import randint
from time import sleep
npensado = randint(0, 5)

print('\033[34m-=\033[m'*22)
print('Estou pensando em um numero entre 0 e 5...')
print('\033[34m-=\033[m'*22)
numero = int(input('Tente adivinhar qual é: '))
print('\033[32mPROCESSANDO.....\033[m')
sleep(2)
if numero == npensado:
    print(f'\033[33mCARACA!!! Que medo de você!! Você é mágico. Pensei exatamente no numero {npensado}!!!\033[m')
else:
    print(f'\033[31mHAHAHA.. GANHEIIII!!! Eu tinha pensado no {npensado}!! Tente de novo!!\033[m')