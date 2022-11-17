# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

# O primeiro valor é MAIOR;
# O Segundo valor é MENOR;
# Não existe valor maior, os dois são IGUAIS.

number_one = int(input('Digite o primeiro número: '))
number_two = int(input('Digite o segundo número: '))

if number_one > number_two:
    print('O primeiro número ({}) é maior que o segundo ({}).'.format(number_one,number_two))
elif number_two > number_one:
    print('O segundo número ({}) é maior que o primeiro ({}).'.format(number_two,number_one))
else:
    print('Os números são iguais!')
