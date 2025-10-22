class animal:
    def falar(self):
        pass

class Cachorro(animal):
    def falar(self):
        return "Osvaldo!"
    
class Gato(animal):
    def falar(self):
        return "Miau!"

class Pato(animal):
    def falar(self):
        return "Quack!"
def fazer_animmal_falar(animal):
    print(animal.falar())

cachorro = Cachorro()
gato = Gato()
pato = Pato()

print("---EXEMPLO 1: POLIMORFISMO COM HERANÇA---\n")
fazer_animmal_falar(cachorro)
fazer_animmal_falar(gato)
fazer_animmal_falar(pato)

print("\n---EXEMPLO 2: POLIMORFISMO COM HERANÇA IMPLICITA---\n")

class Carro:
    def mover(self):
        return "O carro esta dirigindo."
    def ligar_motor(self):
        return "Motor ligado."
class Bicicleta:
    def mover(self):
        return "A bicicleta esta pedalando."
    def tocar_campainha(self):
        return "Trim trim!"
    
def simular_movimento(veiculo):
    """"""
    print(veiculo.mover())

class Pessoa:
    def mover(self):
        return "A pessoa esta andando."

print("\n---EXEMPLO 3: POLIMORFISMO COM DUCK TYPING---\n")

carro = Carro()
bicicleta = Bicicleta()
pessoa = Pessoa()

simular_movimento(carro)
simular_movimento(bicicleta)
simular_movimento(pessoa)
