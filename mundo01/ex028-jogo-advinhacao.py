# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e pessa ao usuário descobrir o número.

from random import randint

number_chosen_computer = randint(0, 5)
user_choice = int(input('Tente acertar o número que pensei entre 0 e 5: '))

if number_chosen_computer == user_choice:
    print(f'''
    Você GANHOU!!!!!!
    O número escolhido por mim foi: {number_chosen_computer}
    ''')
else:
    print(f'''
    Você PERDEU!!!!!!
    O número escolhido por mim foi: {number_chosen_computer}
    ''')
