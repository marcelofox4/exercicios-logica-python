# Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento.
# Para salário superiores a R$ 1.250,00, calcule um aumento de 10%.
# Para salários inferiores ou iguais, o aumento é de 15%.

salary = float(input('Digite o valor do salário para calculo do aumento: '))
increase = 0

if salary <= 1250:
    increase = salary * (15 / 100)
else:
    increase = salary * (10 / 100)

print(f'''
O aumento doi de R$ {increase}
Total do salário é R$ {salary + increase}
''')
