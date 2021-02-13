expr = input(f'Digite sua expressão: ').strip()
lista = []
for simb in expr:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break

if len(lista) == 0:
    print(f'Sua expressão esta correta.')
else:
    print(f'Sua expressão esta incorreta.')
