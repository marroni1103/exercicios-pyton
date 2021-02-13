menos20anos = 0
somaidades = 0
idadehomem = 0
nomehomem = ''
for n in range(1, 5):
    print(f'---------- {n}° Pessoa ----------')
    nome = input('Informe o nome: ').strip()
    idade = int(input('Informe a idade: '))
    sexo = input('Informe o sexo [M / F]: ').strip().lower()
    somaidades += idade
    if idade < 20:
        if sexo == 'f':
            menos20anos += 1
    if sexo == 'm' and idade > idadehomem:
        idadehomem = idade
        nomehomem = nome

mediaidades = somaidades / 4

print(f'A media de idade é de {mediaidades}.')
print(f'O homem mais velho é o {nomehomem} e tem {idadehomem} anos.')
print(f'Existe {menos20anos} mulhere(s) com menos de 20 anos.')
