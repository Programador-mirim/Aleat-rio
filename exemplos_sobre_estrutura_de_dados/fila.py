""" class Fila:
    def __init__(self):
        self.itens = []
    def esta_vazia(self):
        return len(self.itens) == 0
    def enfileirar(self, item):
        self.itens.append(item)
    def desenfileirar(self):
        if self.esta_vazia():
            raise Exception("Fila vazia")
        return self.itens.pop(0) # Remove do início (operação O(n))
    def frente(self):
        if self.esta_vazia():
            raise Exception("Fila vazia")
        return self.itens[0]
    def tamanho(self):
        return len(self.itens)
    def __str__(self):
        return str(self.itens)
# Exemplo de uso
fila = Fila()
fila.enfileirar("Cliente 1")
fila.enfileirar("Cliente 2")
fila.enfileirar("Cliente 3")
print(fila) # ['Cliente 1', 'Cliente 2', 'Cliente 3']
print(fila.frente()) # Cliente 1
cliente = fila.desenfileirar() # Remove e retorna 'Cliente 1'
print(fila) # ['Cliente 2', 'Cliente 3']
print(fila.tamanho()) # 2 """

""" import queue
import threading
import time
# Criando uma fila thread-safe
fila_tarefas = queue.Queue()
# Função para o produtor (adiciona itens à fila)
def produtor():
    for i in range(5):
        item = f"Tarefa {i}"
        fila_tarefas.put(item)
        print(f"Produtor adicionou: {item}")
        time.sleep(0.5)
# Função para o consumidor (processa itens da fila)
def consumidor():
    while True:
# Tenta obter um item, espera até 2 segundos
        try:
            item = fila_tarefas.get(timeout=2)
            print(f"Consumidor processou: {item}")
# Marca a tarefa como concluída
            fila_tarefas.task_done()
            time.sleep(1)
        except queue.Empty:
            print("Fila vazia, consumidor encerrando")
            break
# Criando e iniciando threads
thread_produtor = threading.Thread(target=produtor)
thread_consumidor = threading.Thread(target=consumidor)
thread_produtor.start()
thread_consumidor.start()
thread_produtor.join()
thread_consumidor.join()
print("Todas as tarefas foram processadas") """

""" from collections import deque
import random
import time
class SistemaAtendimento:
    def __init__(self):
        self.fila = deque()
        self.atendimento_atual = None
        self.senha_atual = 0
    def gerar_senha(self):
        self.senha_atual += 1
        nova_senha = f"A{self.senha_atual:03d}"
        self.fila.append(nova_senha)
        print(f"Senha {nova_senha} gerada. Posição na fila: {len(self.fila)}")
        return nova_senha
    def chamar_proximo(self):
        if not self.fila:
            print("Não há clientes na fila")
            return None
        self.atendimento_atual = self.fila.popleft()
        print(f"Chamando senha {self.atendimento_atual} para atendimento")
        return self.atendimento_atual
    def verificar_fila(self):
        if not self.fila:
            print("Fila vazia")
        else:
            print(f"Fila atual: {list(self.fila)}")
            print(f"Clientes aguardando: {len(self.fila)}")
# Simulação de um dia de atendimento
def simular_dia_atendimento():
    sistema = SistemaAtendimento()
# Simulando chegada aleatória de clientes
    for _ in range(10):
        if random.random() < 0.7: # 70% de chance de chegar um novo cliente
                sistema.gerar_senha()
# 50% de chance de realizar um atendimento
        if random.random() < 0.5:
            sistema.chamar_proximo()
    sistema.verificar_fila()
    time.sleep(0.5)
# Atendendo clientes restantes
    print("\nFinalizando expediente, atendendo clientes restantes:")
    while len(sistema.fila) > 0:
        sistema.chamar_proximo()
        time.sleep(0.5)
    print("Todos os clientes foram atendidos!")
# Executar simulação
simular_dia_atendimento() """

import heapq
class FilaPrioridade:
    def __init__(self):
        self.fila = []
        self.indice = 0 # Para desempate quando prioridades são iguais
    def inserir(self, item, prioridade):
# Prioridades menores são atendidas primeiro
        heapq.heappush(self.fila, (prioridade, self.indice, item))
        self.indice += 1
    def remover(self):
        if not self.fila:
            raise Exception("Fila vazia")
        return heapq.heappop(self.fila)[2] # Retorna apenas o item
    def esta_vazia(self):
        return len(self.fila) == 0
# Exemplo: Triagem de pacientes em hospital
fila_hospital = FilaPrioridade()
fila_hospital.inserir("Paciente A - Dor no peito", 1) # Emergência
fila_hospital.inserir("Paciente B - Corte superficial", 3) # Não urgente
fila_hospital.inserir("Paciente C - Fratura exposta", 2) # Urgente
fila_hospital.inserir("Paciente D - Febre alta", 2) # Urgente
# Atendimento por ordem de prioridade
while not fila_hospital.esta_vazia():
    proximo = fila_hospital.remover()
    print(f"Atendendo: {proximo}")