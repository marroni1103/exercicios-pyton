vel = int(input('Informe a velocidade do carro: '))
multa = 7
if vel > 80:
    excesso = vel - 80
    valmulta = excesso * multa
    print(f'MULTADO!!! O limite de velocidade é de 80Km/h. \nO valor a pagar de multa é de R$ {valmulta:.2f}.')
else:
    print('Muito bem.. motorista exemplar. Continue assim!!!')