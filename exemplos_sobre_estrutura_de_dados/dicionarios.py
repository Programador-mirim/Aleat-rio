""" # Dicionário vazio
dicionario_vazio = {}
# Dicionário com pares chave-valor
aluno = {
'nome': 'Pedro Silva',
'idade': 22,
'curso': 'Ciência da Computação',
'matricula': 20230045
}
# Dicionário com diferentes tipos de chaves
diversos = {
42: 'resposta',
'pi': 3.14159,
(1, 2): 'coordenada',
True: 'booleano'
}

print(dicionario_vazio)
print(aluno)
print(diversos) """

# Criando um dicionário de produtos
produtos = {
'notebook': 3500,
'smartphone': 2800,
'tablet': 1500,
'fones': 300
}
# Acessando valores
preco_notebook = produtos.get('notebook') # 3500
preco_camera = produtos.get('camera', 'Produto não encontrado') # 'Produto não encontrado'
# Iterando sobre chaves
for produto in produtos.keys():
    print(f"Produto disponível: {produto}")
# Iterando sobre valores
for preco in produtos.values():
    print(f"Preço: R$ {preco}")
# Iterando sobre pares chave-valor
for produto, preco in produtos.items():
    print(f"{produto}: R$ {preco}")
# Atualizando o dicionário
novos_produtos = {'camera': 1200, 'impressora': 800}
produtos.update(novos_produtos)
# produtos agora inclui 'camera' e 'impressora'
# Removendo itens
preco_tablet = produtos.pop('tablet') # preco_tablet = 1500, 'tablet' removido
ultimo_item = produtos.popitem() # Remove o último item adicionado ('impressora': 800)