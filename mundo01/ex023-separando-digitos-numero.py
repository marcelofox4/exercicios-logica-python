# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
# Ex: 1834, unidade = 4, dezena = 3, centena = 8, milhar = 1

number = int(input('Digite um número entre 0 e 9999: '))
unit = number // 1 % 10
ten = number // 10 % 10
hundred = number // 100 % 10
thousand = number // 1000 % 10

print(f'''
unidade: {unit}
dezena: {ten}
centena {hundred}
milhar: {thousand}
''')
