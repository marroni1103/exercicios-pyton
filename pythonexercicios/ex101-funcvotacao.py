def voto(num):
    from datetime import date
    anoatual = date.today().year
    idade = anoatual - num
    if idade < 16:
        return f"Com {idade} anos: NÃO VOTA"
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f"Com {idade} anos: VOTO OBRIGATORIO"


print('-' * 30)
anonasc = int(input('Em que ano você nasceu? '))
print(voto(anonasc))
