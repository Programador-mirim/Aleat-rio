from abc1 import Veiculo
from carro_veiculo import Carro
from moto_veiculo import Moto

meu_carro = Carro("Toyota", "Corolla", 2020, 4)
minha_moto = Moto("Honda", "CB500", 2019, 500)

print(meu_carro.descrever())
print(meu_carro.acelerar(30))
print(meu_carro.buzinar())  # Método herdado da classe abstrata

print(minha_moto.descrever())
print(minha_moto.acelerar(30))
print(minha_moto.empinar())  # Método específico de Mo