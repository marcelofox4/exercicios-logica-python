# Desenvolva um programa que leia um valor em metros e o exiba em centímetros e milímetros.

value_meter = float(input('Digite o valor em metros para conversão: '))
centimeter = value_meter * 100
milimeter = value_meter * 1000

print(f'''
Centímetros = {centimeter:.1f}cm
Milímetros = {milimeter:.1f}mm
''')