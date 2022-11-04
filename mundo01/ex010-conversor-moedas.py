# Crie um programa que leia uma quantia de dinheiro em reais e exiba em dolar.

brazilian_real = float(input('Digite o valor em reais para ser convertido: '))
dollar_conversion = brazilian_real / 5.03

print('Valor em Dólar americano é: US$ {:.2f}'.format(dollar_conversion))
