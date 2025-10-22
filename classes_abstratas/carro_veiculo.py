from abc1 import Veiculo

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