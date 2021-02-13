medida = input('Para qual temperatura vc quer converter? °C ou °F? ').lower()
if medida == 'f':
    c = float(input('Informe a temperatura em °C: '))
    f = ((9 * c) / 5) + 32
    print(f'A temperatura de {c}°C equivale a {f:.1f}°F.')
else:
    f = float(input('Informe a temperatura em °F: '))
    c = (f - 32) / 1.8
    print(f'A temperatura de {f}°F equivale a {c:.1f}°C.')
