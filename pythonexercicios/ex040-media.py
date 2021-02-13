n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segnda nota: '))

media = (n1 + n2) / 2

if media < 5.0:
    print(f'\033[31mREPROVADO\033[m!!!. Sua média foi de {media:.1f}.')
elif 5.0 <= media <= 6.9:
    print(f'\033[33mRECUPERAÇÃO\033[m!!!. Sua média foi de {media:.1f}')
else:
    print(f'\033[32mAPROVADO\033[m!!!. Sua média foi de {media:.1f}')