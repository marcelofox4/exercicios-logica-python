# Crie um programa que leia duas notas do aluno e calcule sua média, mostrando uma mensagem no final, de acordo com média atingida:

# Média abaixo de 5.0 = REPROVADO;
# Média entre 5.0 e 6.9 = RECUPERAÇÃO;
# Média 7.0 ou superior: APROVADO;

student_grade_one = float(input('Digite a primeira nota: '))
student_grade_two = float(input('Digite a segunda nota: '))
average = (student_grade_one + student_grade_two) / 2

if average < 5:
    print('Sua média é {:.1f} - REPROVADO'.format(average))
elif average >= 5 and average <= 6.9:
    print('Sua média é {:.1f} - RECUPERAÇÃO'.format(average))
elif average >= 7:
    print('Sua média é {:.1f} - APROVADO'.format(average))
else:
    print('Sua média não consta nas especificaçõs do sistema!')
