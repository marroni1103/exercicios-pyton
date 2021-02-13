cidade = input('Informe o nome da cidade: ').strip()
cidade = cidade.lower().split()
if cidade[0] == 'santo':
    print(f'O primeiro nome da sua cidade é Santo')
else:
    print('Sua cidade não começa com Santo')