nome = input('Informe seu nome completo: ').strip()

print(f'Seu nome tudo em maiusculo é {nome.upper()}')
print(f'Seu nome tudo em minusculo é {nome.lower()}')
novo_nome = nome.split()
print(f'Seu nome tem {len(nome) - nome.count(" ")} caracteres sem contas os espaços')
print(f'Seu primeiro nome tem {len(novo_nome[0])} caracteres')