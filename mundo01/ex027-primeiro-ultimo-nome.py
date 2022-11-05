# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e último nome separadamente.

name_complete = input('Digite seu nome completo: ').strip()
cut_name = name_complete.split()

print(f'''
Primeiro nome: {cut_name[0]}
Último nome: {cut_name[-1]}
''')
