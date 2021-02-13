listapesos = []
for c in range(1, 6):
    peso = float(input(f'Informe o peso da {c}° pessoa: '))
    listapesos.append(peso)

print(f'O menor peso informado foi {min(listapesos)}kg')
print(f'O maior peso informado foi {max(listapesos)}kg')
