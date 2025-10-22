import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Terceira Janela: Uso de messagebox")

def exibir_mensagem():
    messagebox.showinfo(title="Informação", message="Olá mundo!:")

botao_mensagem = tk.Button(janela, text="Clique em MIM", command=exibir_mensagem)
botao_mensagem.pack(pady=20)

janela.mainloop()