""" # Tupla vazia
tupla_vazia = ()
# Tupla com um único elemento (observe a vírgula obrigatória)
tupla_unitaria = (42,)
# Tupla com múltiplos elementos
coordenadas = (10, 20)
pessoa = ('João', 30, 'Engenheiro')
# Tupla aninhada
matriz = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

print(tupla_vazia)
print(tupla_unitaria)
print(coordenadas)
print(pessoa)
print(matriz) """ 

""" coordenadas = (10, 20, 30, 40, 50)
# Acesso por índice
x = coordenadas[0] # x = 10
y = coordenadas[1] # y = 20
# Fatiamento
subconjunto = coordenadas[1:4] # (20, 30, 40)
# Verificação de existência
existe = 30 in coordenadas # existe = True
# Métodos disponíveis
ocorrencias = coordenadas.count(30) # ocorrencias = 1
posicao = coordenadas.index(40) # posicao = 3

print(x)
print(y)
print(subconjunto)
print(existe)
print(ocorrencias)
print(posicao) """

""" dados = ('Python', 2023, 'Estruturas', 'Dados')
# Acesso por índice
primeiro = dados[0] # 'Python'
ultimo = dados[-1] # 'Dados'
# Fatiamento
subtupla = dados[1:3] # (2023, 'Estruturas')
primeiros_dois = dados[:2] # ('Python', 2023)
ultimos_dois = dados[-2:] # ('Estruturas', 'Dados')

print(primeiro)
print(ultimo)
print(subtupla)
print(primeiros_dois)
print(ultimos_dois) """

""" # Tupla original
tupla_original = (10, 20, 30, 40)
# Conversão para lista
lista = list(tupla_original)
# Modificações na lista
lista.append(50)
lista[0] = 15
# Conversão de volta para tupla
nova_tupla = tuple(lista) # (15, 20, 30, 40, 50)

print(tupla_original)
print(nova_tupla) """
