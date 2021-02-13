frase = input('Informe uma frase para ver se é palíndromo: ').strip().lower()
frasejunta = frase.split()
frasejunta = ''.join(frasejunta)
novafrase = frasejunta[::-1]

print(f'O inverso de {frasejunta} é {novafrase}')

if frasejunta == novafrase:
    print(f'A frase informada é um palíndromo.')
else:
    print(f'A frase informada não é um palindromo.')

