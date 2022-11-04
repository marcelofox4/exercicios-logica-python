# Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possíveis sobre ele.

message = input('Digite algo: ')

print(f'''
O tipo primitivo é: {type(message)}
Só tem espeços: {message.isspace()}
É um número: {message.isnumeric()}
É alfabético: {message.isalpha()}
É alfanúmerico: {message.isalnum()}
Está em maiscúla: {message.isupper()}
Está em minúscula: {message.islower()}
Está capitalizada: {message.istitle()}
''')