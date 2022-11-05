# Faça um programa que leia 3 números e mostre qual é o menor e qual é o maior.

number_one = int(input('Digite o primeiro número: '))
number_two = int(input('Digite o segundo número: '))
number_three = int(input('Digite o terceiro número: '))

if number_one > number_two and number_one > number_three:
    print('O número MAIOR é: {}'.format(number_one))
    if number_two > number_three:
        print('O número MENOR é: {}'.format(number_three))
    else:
        print('O número MENOR é: {}'.format(number_two))

if number_two > number_one and number_two > number_three:
    print('O número MAIOR é: {}'.format(number_two))
    if number_one > number_three:
        print('O número MENOR é: {}'.format(number_three))
    else:
        print('O número MENOR é: {}'.format(number_one))

if number_three > number_one and number_three > number_two:
    print('O número MAIOR é: {}'.format(number_three))
    if number_two > number_one:
        print('O número MENOR é: {}'.format(number_one))
    else:
        print('O número MENOR é: {}'.format(number_two))
