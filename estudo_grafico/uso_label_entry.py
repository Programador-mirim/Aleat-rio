import tkinter as tk
from tkinter import messagebox

#Cria a janela principal.
tela = tk.Tk()
tela.title("Quarta janela: Uso de label e entry")

#Função para exibir o nome e sobrenome em um mensagembox.
def exibir_nome():
    nome = entrada_nome.get()
    sobrenome = entrada_sobrenome.get()
    if nome:
        messagebox.showinfo("Nome informado", f"Olá, {nome} {sobrenome}!")
    else:
        messagebox.showwarning("Entrada vazia", "Por favor, informe um nome.")

#criar um rótulo (label) para instruir o usuário.
rotulo1 = tk.Label(tela, text="Digite seu nome:")
rotulo1.pack(pady=10)
entrada_nome = tk.Entry(tela,  width=50)
entrada_nome.pack(pady=10)


rotulo2 = tk.Label(tela, text="Digite seu sobrenome:")
rotulo2.pack(pady=10)
#criar um campo de entrada (entry) de dados de janela.
entrada_sobrenome = tk.Entry(tela,  width=50)
entrada_sobrenome.pack(pady=10)

#criar um botão para exibir o nome informado.
botao_exibir = tk.Button(tela, text="Exibir nome", command=exibir_nome)
botao_exibir.pack(pady=10)

#executar a janela.
tela.mainloop()

