from math import hypot

lado1 = float(input('Informe o cateto oposto: '))
lado2 = float(input('Informe o cateto adjacente: '))

print(f'Para os dados informados {lado1}x{lado2} a Hipotenusa é {hypot(lado1, lado2):.2f}')