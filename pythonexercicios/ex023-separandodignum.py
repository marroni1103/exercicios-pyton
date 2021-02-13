num = int(input('Informe um numero entre 0 e 9999: '))
u = num // 1 % 10 # pega o ultimo numero (unidade)
d = num // 10 % 10 # pega o numero referente a dezena
c = num // 100 % 10 # pega o numero referente a centena
m = num // 1000 % 10 # pega o numero referente ao milhar

print(f'Analisando seu numero {num}')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')