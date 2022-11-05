# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retangulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot

opposite_side = float(input('Digite o comprimento do cateto oposto: '))
adjacent_side = float(input('Digite o comprimento do cateto adjacente: '))
hypotenuse = hypot(opposite_side, adjacent_side)

print('O calculo do comprimento da Hipotenusa é {:.2f}'.format(hypotenuse))
