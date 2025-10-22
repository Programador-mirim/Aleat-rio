""" class Pilha:
    def __init__(self):
        self.itens = []
    def esta_vazia(self):
        return len(self.itens) == 0
    def push(self, item):
        self.itens.append(item)
    def pop(self):
        if self.esta_vazia():
            raise Exception("Pilha vazia")
        return self.itens.pop()
    def topo(self):
        if self.esta_vazia():
            raise Exception("Pilha vazia")
        return self.itens[-1]
    def tamanho(self):
        return len(self.itens)
    def __str__(self):
        return str(self.itens)
# Exemplo de uso
pilha = Pilha()
pilha.push(10)
pilha.push(20)
pilha.push(30)
print(pilha) # [10, 20, 30]
print(pilha.topo()) # 30
item = pilha.pop() # Remove e retorna 30
print(pilha) # [10, 20]
print(pilha.tamanho()) # 2 """

class EditorTexto:
    def __init__(self):
        self.texto = ""
        self.historico = [] # Pilha de estados anteriores
    def inserir(self, texto_novo):
        self.historico.append(self.texto) # Salva estado atual
        self.texto += texto_novo
        print(f"Texto atual: {self.texto}")
    def apagar(self, n_caracteres):
        if n_caracteres <= len(self.texto):
            self.historico.append(self.texto) # Salva estado atual
            self.texto = self.texto[:-n_caracteres]
            print(f"Texto atual: {self.texto}")
        else:
            print("Não há caracteres suficientes para apagar")
    def desfazer(self):
        if self.historico:
            self.texto = self.historico.pop()
            print(f"Ação desfeita. Texto atual: {self.texto}")
        else:
            print("Não há ações para desfazer")
# Exemplo de uso
editor = EditorTexto()
editor.inserir("Olá ") # Texto atual: Olá
editor.inserir("mundo!") # Texto atual: Olá mundo!
editor.apagar(7) # Texto atual: Olá
editor.desfazer() # Ação desfeita. Texto atual: Olá mundo!
editor.desfazer() # Ação desfeita. Texto atual: Olá
editor.desfazer() # Ação desfeita. Texto atual:
editor.desfazer() # Não há ações para desfazer