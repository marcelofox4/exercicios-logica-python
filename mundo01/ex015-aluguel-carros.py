# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa 60,00 reais por dia e 15 centavos por Km rodado.

rented_days = int(input('Digite a quantidade de dias que o carro foi alugado: '))
kilometers_traveled = float(input('Digite a quantidade de Km rodados: '))
rent_price = (rented_days * 60) + (kilometers_traveled * 0.15)

print('O preço do aluguel do carro é R$ {:.2f}'.format(rent_price))
