#Implementação Básica de Árvore Binária de Busca
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None
    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_recursivo(self.raiz, valor)
    def _inserir_recursivo(self, no, valor):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self._inserir_recursivo(no.esquerda, valor)
        else:
            if no.direita is None:
                no.direita = No(valor)
            else:
                self._inserir_recursivo(no.direita, valor)
    def buscar(self, valor):
            return self._buscar_recursivo(self.raiz, valor)
    def _buscar_recursivo(self, no, valor):
        if no is None or no.valor == valor:
            return no is not None
        if valor < no.valor:
            return self._buscar_recursivo(no.esquerda, valor)
        return self._buscar_recursivo(no.direita, valor)
    def percurso_em_ordem(self):
        resultado = []
        self._percurso_em_ordem_recursivo(self.raiz, resultado)
        return resultado
    def _percurso_em_ordem_recursivo(self, no, resultado):
        if no:
            self._percurso_em_ordem_recursivo(no.esquerda, resultado)
            resultado.append(no.valor)
            self._percurso_em_ordem_recursivo(no.direita, resultado)
    def percurso_pre_ordem(self):
        resultado = []
        self._percurso_pre_ordem_recursivo(self.raiz, resultado)
        return resultado
    def _percurso_pre_ordem_recursivo(self, no, resultado):
        if no:
            resultado.append(no.valor)
            self._percurso_pre_ordem_recursivo(no.esquerda, resultado)
            self._percurso_pre_ordem_recursivo(no.direita, resultado)
    def percurso_pos_ordem(self):
        resultado = []
        self._percurso_pos_ordem_recursivo(self.raiz, resultado)
        return resultado
    def _percurso_pos_ordem_recursivo(self, no, resultado):
        if no:
            self._percurso_pos_ordem_recursivo(no.esquerda, resultado)
            self._percurso_pos_ordem_recursivo(no.direita, resultado)
            resultado.append(no.valor)
        return


# Criando uma árvore binária de busca
arvore = ArvoreBinariaBusca()
# Inserindo valores
valores = [50, 30, 70, 20, 40, 60, 80]
for valor in valores:
    arvore.inserir(valor)
# Visualização conceitual da árvore:
# 50
# / \
# 30 70
# / \ / \
# 20 40 60 80
# Buscando valores
print(f"30 está na árvore? {arvore.buscar(30)}") # True
print(f"35 está na árvore? {arvore.buscar(35)}") # False
# Percursos
print("Percurso em ordem:", arvore.percurso_em_ordem()) # [20, 30, 40, 50, 60, 70, 80]
print("Percurso pré-ordem:", arvore.percurso_pre_ordem()) # [50, 30, 20, 40, 70, 60, 80]
print("Percurso pós-ordem:", arvore.percurso_pos_ordem()) # [20, 40, 30, 60, 80, 70, 50]

def remover(self, valor):
    self.raiz = self._remover_recursivo(self.raiz, valor)

def _remover_recursivo(self, no, valor):
# Caso base: árvore vazia
    if no is None:
        return no
# Navegar pela árvore
    if valor < no.valor:
        no.esquerda = self._remover_recursivo(no.esquerda, valor)
    elif valor > no.valor:
        no.direita = self._remover_recursivo(no.direita, valor)
    else:
# Nó encontrado, realizar remoção
# Caso 1: Nó sem filhos (folha)
        if no.esquerda is None and no.direita is None:
            return None
# Caso 2: Nó com apenas um filho
        elif no.esquerda is None:
            return no.direita
        elif no.direita is None:
            return no.esquerda
# Caso 3: Nó com dois filhos
# Encontrar o sucessor (menor valor na subárvore direita)
    sucessor_valor = self._encontrar_min_valor(no.direita)
    no.valor = sucessor_valor
# Remover o sucessor
    no.direita = self._remover_recursivo(no.direita, sucessor_valor)
    return no
def _encontrar_min_valor(self, no):
    atual = no
# Descer para a extrema esquerda
    while atual.esquerda is not None:
        atual = atual.esquerda
    return atual.valor