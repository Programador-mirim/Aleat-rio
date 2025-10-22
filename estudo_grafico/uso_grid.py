import tkinter as tk

janela = tk.Tk()
janela.title("Usos do grid")
janela.geometry("400x300")

label1 = tk.Label(janela, text="Label 1", font=("Arial", 14, "bold"))
label2 = tk.Label(janela, text="Label 2", font=("Arial", 14, "bold"))
button1 = tk.Button(janela, text="Botão 1", font=("Arial", 14, "bold"), bg="red", fg="blue")
button2 = tk.Button(janela, text="Botão 2", font=("Arial", 14, "bold"), bg="red", fg="blue")

label1.grid(row=0, column=0, padx=10, pady=10)
label2.grid(row=1, column=0, padx=10, pady=10)
button1.grid(row=0, column=1, padx=10, pady=10)
button2.grid(row=1, column=1, padx=10, pady=10)

janela.mainloop()