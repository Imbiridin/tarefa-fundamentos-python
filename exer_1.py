nome_produto = []
preco_produto = []
total = 0

while True:
    produto_nome = input("Digite o nome do produto: ")
    produto_preco = float(input("Digite o preço do produto: "))

    nome_produto.append(produto_nome)   
    preco_produto.append(produto_preco)
    total += produto_preco


    continuar = input("Deseja continuar? (sair/continuar): ").lower()
    if continuar == "sair":
        break

media_produtos = sum(preco_produto) / len(preco_produto)


print("Produtos cadastrados: ", nome_produto)
print("Preços dos produtos: ", preco_produto)
print("Media dos produtos: ", media_produtos)
print("Total: ", total)