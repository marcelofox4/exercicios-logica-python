# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salary = float(input('Digite o salário do funcionário: '))
increase = salary * (15 / 100)
new_salary = salary + increase

print('O salário com o aumento de 15% é R$ {:.2f}'.format(new_salary))
