from datetime import date
trabalhador = {}
trabalhador['nome'] = input(f'Nome: ')
trabalhador['idade'] = int(input(f'Ano de Nascimento: '))
trabalhador['idade'] = date.today().year - trabalhador['idade']
trabalhador['ctps'] = int(input(f'Informe a carteira de trabalho (0 caso nao tenha): '))
if trabalhador['ctps'] != 0:
    trabalhador['contratacao'] = int(input('Ano de contratação: '))
    trabalhador['salario'] = float(input('Informe o Salario: R$ '))
    trabalhador['aposentadoria'] = (35 - (date.today().year - trabalhador['contratacao'])) + trabalhador['idade']

print('-='*20)
for k, v in trabalhador.items():
    print(f'{k} tem o valor {v}')
