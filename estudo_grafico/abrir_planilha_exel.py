import tkinter as tk
from tkinter import ttk
import pandas as pd

def opem_exel_arquivo():
    file_path = r'c:\Users\pusuario\Documents\Pasta1.xlsx'
    df = pd.read_excel(file_path)

    # Limpa a tabela
    for row in tree.get_children():
        tree.delete(row)

    tree["columns"] = list(df.columns)
    tree['show'] = 'headings'

    # Adiciona os cabeçalhos da tabela
    for column in df.columns:
        tree.heading(column, text=column)
        tree.column(column, width=100, anchor='center')

    # Adiciona as linhas da tabela
    for _, row in df.iterrows():
        tree.insert("", "end", values=list(row))

#configurar janela principal
janela = tk.Tk()
janela.title("Visualizador de planilhaas de excel")

#criar botão para abrir planilha
opem_button = tk.Button(janela, text="Abrir planilha", command=opem_exel_arquivo)
opem_button.pack(pady=10)

#criar tabela
tree = ttk.Treeview(janela)
tree.pack(fill="both", expand=True)

janela.mainloop()