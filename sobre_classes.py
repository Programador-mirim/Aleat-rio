#explicação do codigo:

'''
1. Definição da classe "Animal":
- A classe "Animal" é definida com um método construtor "__init__" que recebe os parâmetros: "nome", "especie" e "idade". 
- A classe tambem possui dois metodos "emitir_som" e "obter_descricao".
'''

class Animal:
    def __init__(self, nome, especie, idade):
        """
        Inicializa uma nova instância de Animal.
        Parâmetros:
        nome (str): O nome do animal.
        especie (str): A espécie do animal.
        idade (int): A idade do animal em anos.
        """
        self.nome = nome
        self.especie = especie
        self.idade = idade
    
    def emitir_som(self, som):
        """
        Emitir um som específico.
        Parâmetros:
        som (str): O som que o animal deve emitir.
        """
        print(f"{self.nome} faz: {som}")

    def obter_descricao(self):
        """
        Obter uma descrição do animal.
        Retorna:
        str: Uma descrição do animal.
        """
        return f"{self.nome} é um {self.especie} de {self.idade} anos"

# Criando instâncias da classe Animal
animal1 = Animal("Rex", "Cachorro", 5)
animal2 = Animal("Mingau", "Gato", 3)

animal1.emitir_som("Au au!")
animal2.emitir_som("Miau!")

print(animal1.obter_descricao())
print(animal2.obter_descricao())

class Passaro(Animal):
    def __init__(self, nome, especie, idade, envergadura_asas):
        '''construtor da classe passaro
        parasmetros:
        envergadura_asas (int): a envergadura das asas em cm
        '''
        super().__init__(nome, especie, idade)
        self.envergadura_asas = envergadura_asas
        
    def voar(self):
        '''
        Metodo para simular o voo do passaro
        '''
        print(f"{self.nome} esta voando com uma envergadura de {self.envergadura_asas} cm")

# Criand uma instância da classe Passaro
passaro1 = Passaro("Loro", "Papagaio", 2, 10)
passaro1.voar()

# Usando os métodos da classe Animal
passaro1.emitir_som("Quero biscoito de chocolate!")
print(passaro1.obter_descricao())