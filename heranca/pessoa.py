class Pessoa:
    def __init__(self, nome, idade):
        """
        construtor da classe pessoa.
        Inicializa os atributos nome e idade.
        """
        #Atributos da instância
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")
        
#criando uma instância da classe pessoa
""" pessoa1 = Pessoa("Carlos", 26)
pessoa2 = Pessoa("Maria", 25)
pessoa3 = Pessoa("Dona Benta", 100)

pessoa1.apresentar()
pessoa2.apresentar()
pessoa3.apresentar() """