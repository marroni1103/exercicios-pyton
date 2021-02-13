frase = input('Digite uma frase: ').strip().lower()
print(f'A letra A apareceu {frase.count("a")} na frase')
print(f'A primeira letra A aparece {frase.find("a") + 1}° posição na frase')
print(f'A ultima letra A aparece {frase.rfind("a") + 1}° posição na frase')
