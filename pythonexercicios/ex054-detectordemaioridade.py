from datetime import date
contmaior = 0
contmenor = 0
anoatual = date.today().year
for n in range(1, 8):
    ano = int(input(f'Informe {n}° data de nascimento: '))
    if anoatual - ano >= 21:
        contmaior += 1
    else:
        contmenor += 1

print(f'Das 7 pessoas informadas {contmaior} já são maiores de 21 anos.')
print(f'Das 7 pessoas informadas {contmenor} ainda são menores de 21 anos.')
