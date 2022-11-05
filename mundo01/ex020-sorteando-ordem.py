# O mesmo professor do desafio ex19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome de quatro alunos e mostre a ordem sorteada.

from random import sample

student_one = input('Digite o nome do primeiro aluno: ')
student_two = input('Digite o nome do segundo aluno: ')
student_three = input('Digite o nome do terceiro aluno: ')
student_four = input('Digite o nome do quarto aluno: ')

students = [student_one, student_two, student_three, student_four]
chosen_order = sample(students, k = len(students))

print(chosen_order)
