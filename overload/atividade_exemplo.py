""" criar uma classe que recebe valores (int ou float) e os somar"""
class SomaTudo:
    def __init__(self, *args):
        self.valores = args

    def somar(self):
        return sum(self.valores)

soma = SomaTudo(1, 2, 3, 4, 5.3, 6.7)
print(f"A soma dos valores é: {soma.somar()}")
