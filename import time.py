import time
import keyboard
import random

bpm = int(input('Digite o tempo desejado '))
valor_nota = int(input('Digite o valor da nota 4, 8, 16, 32 ')) * 2
nota = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
diferenca_segundos = (int(bpm) / 60) * valor_nota

while True:
    if keyboard.is_pressed('K'):
        break
    numero = random.randint(0,11)
    time.sleep(diferenca_segundos)
    print(nota[numero])
