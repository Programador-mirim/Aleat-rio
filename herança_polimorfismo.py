class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        raise NotImplementedError("Subclasses devem implementar este método.")
    
    def mover(self):
        print(f"{self.nome} está se movendo.")

class Cachorro(Animal):
    def emitir_som(self):
        print(f"{self.nome} diz: Au au.")

class Gato(Animal):
    def emitir_som(self):
        print(f"{self.nome} diz: Miau.")

class Passaro(Animal):
    def emitir_som(self):
        print(f"{self.nome} diz: KAKAKA! KAKA! KAKAKA!")

    def mover(self):
        print(f"{self.nome} está voando.")
def fazer_animal_emitir_som(animal):
    '''Função para demonstrar o polimorfismo.
    aceita qualquer objeto que seja uma instância de Animal ou uma subclasse dele.
    '''
    animal.emitir_som()
    
# criando instancias das classes
cachorro = Cachorro("Rex")
gato = Gato("Mingau")
passaro = Passaro("Loro")

# demonstrando o polimorfismo
animais = [cachorro, gato, passaro]

for bicho in animais:
    fazer_animal_emitir_som(bicho)

    bicho.mover()

    print("\n")