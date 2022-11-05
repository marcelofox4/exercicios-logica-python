# Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome.

name = input('Digite seu nome: ').strip()
is_have_silva =  'SILVA' in name.upper()

print('Você tem Silva no nome? {}'.format(is_have_silva))
