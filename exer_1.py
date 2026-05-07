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

caro = max(preco_produto)

quantidade_caros = 0
for preco in preco_produto:
    if preco >= 100:
        quantidade_caros += 1

if quantidade_caros > 1:
    print(f"Muitos produtos caros ({quantidade_caros} produtos)")

print("-" * 50)
print("O produto mais caro:", caro)
print("Produtos cadastrados: ", nome_produto)
print("Preços dos produtos: ", preco_produto)
print("Media dos produtos: ", f"{media_produtos:.2f}")
print("Produtos acima de R$100,00:", quantidade_caros)
print("Total: ", total)
print("-" * 50)
