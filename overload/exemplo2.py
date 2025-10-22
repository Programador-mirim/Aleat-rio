""" POLIMORFISMO: SOBRECARGA - Parametros Opicionais
"""
class CalculadoraSimples:
    def somar(self, a, b, c=None):
        if c is not None:
            return a + b + c
        else:
            return a + b
print("---EXEMPLO 1: Parametros Opicionais---\n")
calc= CalculadoraSimples()
print(f"A soma de 5 + 3: {calc.somar(5, 3)}")
print(f"A soma de 5 + 3 + 2: {calc.somar(5, 3, 2)}")

print("------------------------------------------\n")
""" POLIMORFISMO: SOBRECARGA - Verificação de tipo er lógica condicional
"""
class Exibidor:
    def exibir(self, dado):
        if isinstance(dado, int):
            print(f"Numero inteiro: {dado}")
        elif isinstance(dado, float):
            print(f"Numero real: {dado}")
        elif isinstance(dado, str):
            print(f"Texto: {dado}")
        elif isinstance(dado, bool):
            print(f"Dado Booleano: {dado}")
        elif isinstance(dado, list):
            print(f"Lista de itens: {','.join(map(str, dado))}")
        else:
            print(f"Tipo não reconhecido: {type(dado)}")

print("---EXEMPLO 2: Verificação de tipo e lógica condicional---\n")

exib = Exibidor()
exib.exibir(256)
exib.exibir(3.14)
exib.exibir("Olá mundo")
exib.exibir(True or False)
exib.exibir([1, 2, 3, 4, 5])

print("------------------------------------------\n")
""" POLIMORFISMO: SOBRECARGA - Argumentos Variaveis (*arg e **kwargs)
"""
class ProcessadorDeDados:
    def processar(self, *args, **kwargs):
        if args and not kwargs:
            if all(isinstance(args,(int, float)) for args in args):
                print(f"Somando todos os argumentos: {sum(args)}")
            else:
                print(f"Processando lista de itens: {list(args)}")
        elif kwargs and not args:
            print(f"Processando informações nomeadas:")
            for key, value in kwargs.items():
                print(f"{key}:{value}")
            else:
                print(f"Nenhum argumento ou combinação suportada")

print("---EXEMPLO 3: *args e **kwargs---\n")

proc = ProcessadorDeDados()
proc.processar(1, 2, 3, 4, 5)
proc.processar("A", "B", "C")
proc.processar(nome="John", idade=30, cidade="New York")
print("------------------------------------------\n")
""" POLIMORFISMO: SOBRECARGA - Utilizando functools.singleedispatch
Este é mais avançado e é o ideal quando o comportamento depende do tipo do primeiro argumento.
"""
