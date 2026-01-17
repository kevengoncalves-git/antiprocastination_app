print("Bem vindo ao app Anti-Procastinação!")

from tkinter import *

janela_principal = Tk()
janela_principal.title("App Anti-Procastinação")
janela_principal.geometry('600x450')
janela_principal.config(bg='#0f132e')
janela_principal.resizable(True, True)

#Frame de origem
frame_principal = Frame(janela_principal,bg='#536D88', height=500, width=400)
frame_principal.pack(pady=10, padx=10, fill='both', expand=True)
frame_principal.pack_propagate(False)

# 1. Widget de Texto
label_titulo = Label(
    frame_principal, 
    text="Aplicativo anti-procastinação", 
    bg='#F7DECE',      # Mesma cor do frame para ficar "transparente"
    fg='black',        # Cor da letra
    font=("Verdana", 14, "bold"), 
    relief='sunken'
)
label_titulo.pack(pady=10)

# 2. Widget de conteúdos principal
frame_conteudo_principal = Frame(frame_principal, bg='#D9D9D9', height=310, width=380)
frame_conteudo_principal.pack(pady=1)
frame_conteudo_principal.pack_propagate(False) # Impede o frame de encolher

# 2.1 Menu de controle de tempo
frame_contole_tempo = Frame(frame_conteudo_principal, bg='#9B9B9B', height=160, width=250)
frame_contole_tempo.pack(pady=10)

janela_principal.mainloop()