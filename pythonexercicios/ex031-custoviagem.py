dist = float(input('Informe a distancia em KM da sua viagem: '))
viagcusta = 0.5
viaglonga = 0.45
print(f'Você esta prestes a começar uma viagem de {dist}km.')
if dist <= 200:
    print(f'O custo da sua viagem é de R$ {dist * viagcusta:.2f}')
else:
    print(f'O custo da sua viagem é de R$ {dist * viaglonga:.2f}')
