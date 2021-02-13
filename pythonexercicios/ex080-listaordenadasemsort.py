lista = []
for c in range(0, 4):
    n = int(input('Digite um numero: '))
    if c == 0 or n > lista[-1]:
        print(f'Numero adicionado ao final da lista.')
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'O numero foi adicionado na posição {pos}.')
                break
            pos += 1

print('-=' * 20)
lista.sort()
print(f'Os valores digitados em ordem foram {lista}')
