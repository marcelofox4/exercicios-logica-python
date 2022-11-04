# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

number = int(input('Digite o número para gerar a tabuada: '))
count = 0

while count <= 10:
    print('{} x {} = {}'.format(number, count, number * count))
    count = count + 1
