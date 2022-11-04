# Desenvolva um programa que leia as duas notas de um aluno, calcule a sua média.

student_grade_one = float(input('Digite a primeira nota do aluno: '))
student_grade_two = float(input('Digite a segunda nota do aluno: '))
average = (student_grade_one + student_grade_two) / 2

print('A média do Aluno é: {:.2f}'.format(average))
