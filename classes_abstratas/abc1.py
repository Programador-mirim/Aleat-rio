from abc import ABC, abstractmethod

# Classe abstrata base
class Veiculo(ABC):
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0
    
    @abstractmethod
    def acelerar(self, incremento):
        """Método para aumentar a velocidade"""
        pass
    
    @abstractmethod
    def frear(self, decremento):
        """Método para diminuir a velocidade"""
        pass
    
    def buzinar(self):
        """Método concreto compartilhado por todos os veículos"""
        return "Beep! Beep!"
    
    @abstractmethod
    def descrever(self):
        """Retorna uma descrição do veículo"""
        pass