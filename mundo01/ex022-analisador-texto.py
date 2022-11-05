# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúscula;
# - O nome com todas as letras minúsculas;
# - Quantas letras ao todo, sem considerar espaços;
# - Quantas letras tem o primeiro nome.

full_name = input('Digite seu nome completo: ').strip()
cut_name = full_name.split()

print(f'''
Letras maiúsculas: {full_name.upper()}
Letras minúsculas: {full_name.lower()}
Quantidade de letras: {len(''.join(cut_name))}
Quantidade de letras no primeiro nome: {len(cut_name[0])}
''')