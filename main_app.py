print("Bem vindo ao app antiprocastinação!")

from tkinter import *

janela_principal = Tk()
janela_principal.title("App antiprocastinação")
janela_principal.geometry('500x370')
janela_principal.config(bg='#0f132e')
janela_principal.resizable(True, True)

frame_principal = Frame(janela_principal,bg='#536D88', height=300, width=300)
frame_principal.pack(pady=10, padx=10, fill='both', expand=True)

# 1. Widget de Texto
label_titulo = Label(
    frame_principal, 
    text="Aplicativo anti-procastinação", 
    bg='#F7DECE',      # Mesma cor do frame para ficar "transparente"
    fg='black',        # Cor da letra
    font=("Verdana", 14, "bold"), 
    relief='sunken'
)
label_titulo.pack(pady=20, padx=10)

janela_principal.mainloop()