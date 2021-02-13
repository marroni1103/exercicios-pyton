from time import sleep
import emoji
print('-='*11)
print('Contador de lançamento')
print('-='*11)

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('FELIZ ANO NOVO!!!!')
print(emoji.emojize(':fireworks:, :fireworks:, :fireworks:', use_aliases=True))