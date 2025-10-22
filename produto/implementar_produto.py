from produto import Produto

produto1 = Produto("Smartphone", 5000, 10)
produto2 = Produto("Tablet", 3000, 5)
produto3 = Produto("Notebook", 8000, 3)

produto1.vender(2)
produto2.vender(3)
produto3.vender(1)

produto1.adicionar_produto(5)
produto2.adicionar_produto(10)
produto3.adicionar_produto(2)

print(produto1)
print(produto2)
print(produto3)

print(f"Valor total de estoque: R${produto1.calcular_valor_total():.2f}")
print(f"Valor total de estoque: R${produto2.calcular_valor_total():.2f}")
print(f"Valor total de estoque: R${produto3.calcular_valor_total():.2f}")

""" 
print(f"Disponibilidade do produto 1: {produto1.esta_disponivel()}")
print(f"Disponibilidade do produto 2: {produto2.esta_disponivel()}")
print(f"Disponibilidade do produto 3: {produto3.esta_disponivel()}")
"""
