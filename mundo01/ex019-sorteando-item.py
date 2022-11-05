# Um professor quer sortear um dos seus alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo o nome do escolhido.

from random import choice

student_one = input('Digite o nome do primeiro aluno: ')
student_two = input('Digite o nome do segundo aluno: ')
student_three = input('Digite o nome do terceiro aluno: ')
student_four = input('Digite o nome do quarto aluno: ')

students = [student_one, student_two, student_three, student_four]
chosen_student = choice(students)

print('O aluno escolhido para apagar o quadro é {}.'.format(chosen_student))
