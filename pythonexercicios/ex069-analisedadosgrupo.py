mais18 = homens = mulheresmenos20 = 0
while True:
    sexo = ' '
    continuar = ' '
    print('-'*20)
    print(f'CADASTRE UM PESSOA')
    print('-'*20)
    idade = int(input('IDADE: '))
    while sexo not in 'MF':
        sexo = input('SEXO [M/F]: ').strip().upper()[0]
    if sexo == 'M':
        homens += 1
    if idade >= 18:
        mais18 += 1
    if idade < 20 and sexo == 'F':
        mulheresmenos20 += 1
    print('-' * 20)
    while continuar not in 'NS':
        continuar = input('Deseja continuar [S/N]: ').strip().upper()[0]
    if continuar == 'N':
        break

print(f""" ======== FIM DO PROGRAMA ========    
Foram cadastradas {mais18} pessoas com mais de 18 anos.
Foram cadastradas {homens} homens.
Foram cadastradas {mulheresmenos20} mulheres com menos de 20 anos.""")
