from abc1 import Veiculo

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
