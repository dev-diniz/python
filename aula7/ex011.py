#Desconto produto
preco = float(input('Digite o preco do produto: '))
desc = (preco * 5)/100
novoPreco = preco - desc

print('O preço do produto com desconto de {:.2f}R$ é de {:.2f}R$'.format(desc, novoPreco))
