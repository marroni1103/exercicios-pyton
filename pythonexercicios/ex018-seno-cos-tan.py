import math
an = float(input('Informe o angulo: '))
angulo = math.radians(an)
print(f'Para o angulo {an}°:\nSeno: {math.sin(angulo):.2f}'
      f'\nCosseno: {math.cos(angulo):.2f}\nTangente: {math.tan(angulo):.2f}')