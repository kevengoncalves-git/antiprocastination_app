import time


def temporizador(tempo_limite, label_editada):
    #cronometro simples
    if tempo_limite >= 0:
        minutos_atual = tempo_limite // 60
        segundos_atual = tempo_limite % 60
        timer_formatado = f'{minutos_atual:02}:{segundos_atual:02}'
        #editando a label com o tempo formatado usando config
        label_editada.config(text=timer_formatado)
        #chamando a função recursivamente após 1 seg == 1000miliseg
        #atualiza a label e reduz em 1seg o tempo
        label_editada.after(1000, temporizador, tempo_limite - 1, label_editada)
    else:
        #xinga o cara
        label_editada.config(font=("Verdana", 14, "bold"), fg='red', text='Mais tempo vadio')