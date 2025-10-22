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

# Classe concreta que implementa Veiculo
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, portas):
        super().__init__(marca, modelo, ano)
        self.portas = portas
    
    def acelerar(self, incremento):
        self.velocidade += incremento
        return f"Carro acelerando para {self.velocidade} km/h"
    
    def frear(self, decremento):
        self.velocidade = max(0, self.velocidade - decremento)
        return f"Carro freando para {self.velocidade} km/h"
    
    def descrever(self):
        return f"Carro {self.marca} {self.modelo} ({self.ano}) com {self.portas} portas"

# Outra classe concreta
class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas
    
    def acelerar(self, incremento):
        self.velocidade += incremento * 1.2  # Motos aceleram mais rápido
        return f"Moto acelerando para {self.velocidade} km/h"
    
    def frear(self, decremento):
        self.velocidade = max(0, self.velocidade - decremento)
        return f"Moto freando para {self.velocidade} km/h"
    
    def descrever(self):
        return f"Moto {self.marca} {self.modelo} ({self.ano}) de {self.cilindradas}cc"
    
    def empinar(self):
        return "Empinando a moto! (não faça isso no trânsito real)"

# Uso das classes concretas
meu_carro = Carro("Toyota", "Corolla", 2020, 4)
minha_moto = Moto("Honda", "CB500", 2019, 500)

print(meu_carro.descrever())
print(meu_carro.acelerar(30))
print(meu_carro.buzinar())  # Método herdado da classe abstrata

print(minha_moto.descrever())
print(minha_moto.acelerar(30))
print(minha_moto.empinar())  # Método específico de Moto