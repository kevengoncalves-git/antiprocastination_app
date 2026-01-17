import time

def temporizador():
    string_tempo_limite = '01:00'
    lista_temporal=string_tempo_limite.split(':')
    minutos = int(lista_temporal[0])
    segundos = int(lista_temporal[1])
    total_segundos = minutos * 60 + segundos
    while total_segundos >= 0:
        minutos_atual = total_segundos // 60
        segundos_atual = total_segundos % 60
        timer_formatado = f'{minutos_atual:02}:{segundos_atual:02}'
        print(timer_formatado, end='\r') #\r pra reescrever encima do mesmo print
        time.sleep(1)
        total_segundos -= 1