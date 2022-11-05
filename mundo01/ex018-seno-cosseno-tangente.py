# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

angle = float(input('Digite o valor do ângulo: '))
sine = sin(radians(angle))
cosine = cos(radians(angle))
tangent = tan(radians(angle))

print(f'''
Seno: {sine:.2f}
Cosseno: {cosine:.2f}
Tangente: {tangent:.2f}
''')
