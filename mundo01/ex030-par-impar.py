# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.

number = int(input('Digite um número: '))

if number % 2 == 0:
    print('O número {} é PAR!'.format(number))
else:
    print('O número {} é ÍMPAR'.format(number))
