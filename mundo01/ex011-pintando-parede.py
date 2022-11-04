# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la sabendo que cada litro de tinta, pinta uma área de 2m².

width = float(input('Digite a largura da parede em metros: '))
height = float(input('Digite a altura da parede em metros: '))
area = width * height
amount_ink = area / 2

print(f'''
A quantidade de tinta para pintar uma parede de {area:.1f}m² será de {amount_ink:.1f}l.
''')