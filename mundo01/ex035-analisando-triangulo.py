# Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo.

side_a = float(input('Digite o comprimento da primeira reta: '))
side_b = float(input('Digite o comprimento da segunda reta: '))
side_c = float(input('Digite o comprimento da terceira reta: '))

if side_a + side_b > side_c and side_a + side_c > side_b and side_c + side_b > side_a:
    print('É um triângulo!')
else:
    print('Não é um triângulo!')
