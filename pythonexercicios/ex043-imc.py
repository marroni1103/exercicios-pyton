print('\033[32m-=\033[m'*10)
print('Calculo de IMC')
print('\033[32m-=\033[m'*10)
peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))

imc = peso / (altura * altura)

print(f'Seu IMC é de {imc:.1f}')
if imc < 18.5:
    print('Abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print(f'Sobrepeso')
elif 30 <= imc < 40:
    print(f'Obesidade')
else:
    print(f'Obesidade Morbida')
