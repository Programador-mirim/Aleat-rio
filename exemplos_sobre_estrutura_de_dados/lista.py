""" imprimindo uma linhasmatriz 4x4. """

matriz = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
for linha in matriz:
    print(linha,",")
#explicação/comentário:
#Aqui estamos percorrendo a matriz e imprimindo cada linha individualmente, separadas por vírgulas.
print("\n")
"""a=int(input("Indique uma linha: "))
b=int(input("Indique uma coluna: "))
print(f"O valor corespondente a essa localização { a } e { b } é {matriz[a][b]}")"""
#diagonal dois
print("\n")
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if i == j:
            print(matriz[i][j], end=" ")

print("\n")
#diagonal um
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if i + j == len(matriz) - 1:
            print(matriz[i][j], end=" ")


""" # Criando uma lista
numeros = [10, 5, 8, 3]
# Adicionando elementos
numeros.append(7) # [10, 5, 8, 3, 7]
numeros.extend([1, 2]) # [10, 5, 8, 3, 7, 1, 2]
numeros.insert(1, 20) # [10, 20, 5, 8, 3, 7, 1, 2]
# Removendo elementos
numeros.remove(5) # [10, 20, 8, 3, 7, 1, 2]
ultimo = numeros.pop() # ultimo = 2, numeros = [10, 20, 8, 3, 7, 1]
numeros.pop(1) # numeros = [10, 8, 3, 7, 1]
# Buscando e contando
posicao = numeros.index(7) # posicao = 3
ocorrencias = numeros.count(10) # ocorrencias = 1
# Ordenando e invertendo
numeros.sort() # [1, 3, 7, 8, 10]
numeros.reverse() # [10, 8, 7, 3, 1]

print(numeros) """