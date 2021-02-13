from datetime import date

print('\033[1;32m-=-\033[m'*12)
print(f'Sistema da Confederação de Natação')
print('\033[1;32m-=-\033[m'*12)

anonasc = int(input('Informe seu ano de nascimento: '))

anoatual = date.today().year

idade = anoatual - anonasc
print(f'O atleta tem {idade} anos em {anoatual}.')
if idade <= 9:
    print(f'Categoria do atleta: \033[34mMIRIM\033[m')
elif idade <= 14:
    print(f'Categoria do atleta: \033[34mINFANTIL\033[m')
elif idade <= 19:
    print(f'Categoria do atleta: \033[34mJUNIOR\033[m')
elif idade <= 25:
    print(f'Categoria do atleta: \033[34mSÊNIOR\033[m')
else:
    print(f'Categoria do atleta: \033[34mMASTER\033[m')
