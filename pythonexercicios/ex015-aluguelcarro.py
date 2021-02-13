dias = int(input('Quantos dias alugado? '))
km = float(input('Quantos KM rodados? '))

custodia = 60
custokm = 0.15

print(f'O total a pagar é de R$ {(dias * custodia) + (km * custokm):.2f}')
