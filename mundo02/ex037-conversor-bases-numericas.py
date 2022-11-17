# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

# 1 para Binário;
# 2 para Octal;
# 3 para Hexadecimal.

number = int(input('Digite um número inteiro para a conversão: '))
print('''Digite a opção para converção:
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal''')
choice = int(input('Digite a sua opção: '))

if choice == 1:
    print('O número {} em Binário é {}'.format(number, bin(number)[2:]))
elif choice == 2:
    print('O número {} em Octal é {}'.format(number, oct(number)[2:]))
elif choice == 3:
    print('O número {} em Hexadecimal é {}'.format(number, hex(number)[2:]))
else:
    print('Escolha Inválida!')
