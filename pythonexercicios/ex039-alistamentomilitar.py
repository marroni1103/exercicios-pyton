from datetime import date

print('\033[34m-=-\033[m'*11)
print('Sistema de alistamento militar.')
print('\033[34m-=-\033[m'*11)

anonasc = int(input('Informe sua data de nascimento: '))
anoatual = date.today().year

idade = anoatual - anonasc

if idade < 18:
    print(f'Você ainda tem {idade} anos. Volte quanto completar 18 anos, ainda falta {18 - idade} anos.')
elif idade == 18:
    print(f'Parabens!! Você ja tem 18 anos. Ja pode se alistar e servir seu País.')
else:
    print(f'Obrogado pelo interesse. Mas como ja tem {idade} você ja passou {idade - 18} anos do alistameneto.')