# Faça um programa no qual o usuário precisa cadastrar as informações de dois produto: código, nome, quantidade e preço.
# No final o programa deve mostrar as informações cadastradas e exibir o valor total das compras.


codigo1 = int(input("Insira o código do produto 1: "))
nome1 = input("Insira o nome do produto 1: ")
qtd1 = float(input("Insira a quantidade desse produto: "))
preco1 = float(input("Insira o preço unitário do produto: "))


codigo2 = int(input("Insira o código do produto 2: "))
nome2 = input("Insira o nome do produto 2: ")
qtd2 = float(input("Insira a quantidade desse produto: "))
preco2 = float(input("Insira o preço unitário do produto: "))


total1 = qtd1 * preco1
total2 = qtd2 * preco2


print("\nInformações do Produto 1:")
print(f"Código do produto: {codigo1}")
print(f"Nome: {nome1}")
print(f"Quantidade: {qtd1}")
print(f"Preço unitário: {preco1}")
print(f"Valor total: {total1}")

print("\nInformações do Produto 2:")
print(f"Código do produto: {codigo2}")
print(f"Nome: {nome2}")
print(f"Quantidade: {qtd2}")
print(f"Preço unitário: {preco2}")
print(f"Valor total: {total2}")


valor_total_compras = total1 + total2
print(f"\nValor total das compras: {valor_total_compras}")