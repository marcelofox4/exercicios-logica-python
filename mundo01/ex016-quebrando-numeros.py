# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira.

from math import trunc

number = float(input('Digite um número real: '))

print('A porção inteira do número é {}'.format(trunc(number)))
