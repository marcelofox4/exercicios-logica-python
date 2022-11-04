# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

product_price = float(input('Digite o preço do produto para o descontos: '))
discount = product_price * (5 / 100)
new_product_price = product_price - discount

print('O valor do produto com o desconto de 5% é R$ {:.2f}'.format(new_product_price))