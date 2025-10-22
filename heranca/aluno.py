from pessoa import Pessoa
class Aluno(Pessoa): # type: ignore
    def __init__(self, nome, idade, matricula):
        #Chama o construtor da classe Pessoa para inicializar os atributos nome e idade
        super().__init__(nome, idade)
        self.matricula = matricula
        
    def apresentar(self):        
        super().apresentar()
        print(f"Minha matricula é: {self.matricula}")
        
""" aluno1 = Aluno("Carlos", 26, "123456")
aluno1.apresentar() """