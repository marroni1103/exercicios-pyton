inicio = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
cont = 1
soma = inicio
somatermos = 10

while cont <= 10:
    print(soma, end=' ')
    soma += razao
    cont += 1
print('-> PAUSA')
maistermos = int(input('\nInforme quantos termos quer ver a mais? ou 0 para sair. '))
somatermos += maistermos
cont = 1
while maistermos != 0:
    cont = 1
    while cont < maistermos+1:
        print(soma, end=' ')
        soma += razao
        cont += 1
    print('-> PAUSA')
    maistermos = int(input('\nInforme quantos numeros quer ver a mais? ou 0 para sair. '))
    somatermos += maistermos
print(f'Progressão finalizada com {somatermos} termos mostrados')
print(f'Obrigado por usar o programa!')
