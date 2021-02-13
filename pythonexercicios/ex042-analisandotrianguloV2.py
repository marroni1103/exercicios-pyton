print('\033[34m-=\033[m'*12)
print('Analisador de Trianulo')
print('\033[34m-=\033[m'*12)

a = float(input('Informe a primeira reta: '))
b = float(input('Informe a segunda reta: '))
c = float(input('Informe a terceira reta: '))

if a + b > c and a + c > b and b + c > a:
    print(f'Com essas retas {a} X {b} X {c} consegeuimos montar um triangulo.')
    if a == b == c:
        print(f'Esse é um triangulo Equilátero.')
    elif a == b and a != c or a == c and a != b:
        print(f'Esse é um triangulo Isósceles.')
    elif a != b and a != c and b != c:
        print(f'Esse é um triangulo Escaleno.')
else:
    print(f'Com essas retas {a} X {b} X {c} NÃO consegeuimos montar um triangulo.')
