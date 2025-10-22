import tkinter as tk
from tkinter import messagebox

#Cria a janela principal.
tela = tk.Tk()
tela.title("Quarta janela: Uso de label e entry")
tela.geometry("400x300")
#Função para exibir a soma de dois numeros.
def exibir_soma():
    primeiro_numero = entrada_primeiro_numero.get()
    segundo_numero = entrada_segundo_numero.get()
    soma = int(primeiro_numero) + int(segundo_numero)
    try:
        label_resultado = tk.Label(tela, text=f"A soma de {primeiro_numero} e {segundo_numero} é: {soma}", font=("Arial", 12, "bold"))    
        label_resultado.pack(pady=10)
    except ValueError:
        label_resultado = tk.Label(tela, text="Erro: Entrada inválida. Por favor, digite um numero válido.", font=("Arial", 12, "bold"), bg="red")
#criar um rótulo (label) para instruir o usuário.
rotulo1 = tk.Label(tela, text="Digite seu primeiro_numero:", font=("Arial", 12, "bold"))
rotulo1.pack(pady=10)
entrada_primeiro_numero = tk.Entry(tela,  width=50)
entrada_primeiro_numero.pack(pady=10)


rotulo2 = tk.Label(tela, text="Digite seu segundo_numero:", font=("Arial", 12, "bold"))
rotulo2.pack(pady=10)
#criar um campo de entrada (entry) de dados de janela.
entrada_segundo_numero = tk.Entry(tela,  width=50)
entrada_segundo_numero.pack(pady=10)

#criar um botão para exibir os numeros informados informado.
botao_exibir = tk.Button(tela, text="Exibir soma", command=exibir_soma, bg="green", fg="white", font=("Arial", 12, "bold"))
botao_exibir.pack(pady=10)

#executar a janela.
tela.mainloop()