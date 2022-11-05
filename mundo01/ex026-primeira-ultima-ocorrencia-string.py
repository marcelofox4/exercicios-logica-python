# Faça um programa que leia uma frase pelo teclado e mostre:
# - Quantas vezes aparece a letra 'A';
# - Em que posição ela aparece na primeira vez;
# - Em que posição ela aparece na última vez;

phrase = input('Digite uma frase qualquer: ').strip()

count_a = phrase.upper().count('A')
position_left_a = phrase.upper().find('A')
position_right_a = phrase.upper().rfind('A')

print(f'''
Foi encontrada {count_a} ocorrências de 'A'.
Foi encontrada a primeira ocorrência de 'A' na posição {position_left_a + 1}.
Foi encontrada a última ocorrência de 'A' na posição {position_right_a + 1}.
''')
