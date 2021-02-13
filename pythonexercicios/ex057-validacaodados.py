sexo = input('Informe o sexo: [m/f] ').strip().lower()[0]
while sexo not in 'mfMF':
    print('Opção invalida!')
    sexo = input('Informe o sexo: [M/F} ').strip().lower()

print('Obrigado')

