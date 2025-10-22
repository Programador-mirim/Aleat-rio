import tkinter as tk

def fechar_janela():
    janela.destroy()

janela = tk.Tk()
janela.title("Janela com botão para fechar")

botao_fechar = tk.Button(janela, text="Fechar", command=fechar_janela)
botao_fechar.pack(pady=20)

janela.mainloop()