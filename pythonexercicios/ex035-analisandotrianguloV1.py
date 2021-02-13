print('-='*20)
print('Analisador de Trianulo')
print('-='*20)

a = float(input('Informe a primeira reta: '))
b = float(input('Informe a segunda reta: '))
c = float(input('Informe a terceira reta: '))

if a + b > c and a + c > b and b + c > a:
    print(f'Com essas retas {a} X {b} X {c} consegeuimos montar um triangulo.')
else:
    print(f'Com essas retas {a} X {b} X {c} NÃO consegeuimos montar um triangulo.')
