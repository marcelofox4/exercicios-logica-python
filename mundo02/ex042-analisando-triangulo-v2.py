# Refaça o desafio dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# Equilátero: Todos os lados iguais;
# Isósceles: Dois lados iguais;
# Escaleno: Todos os lados diferentes.

side_a = float(input('Digite o comprimento da primeira reta: '))
side_b = float(input('Digite o comprimento da segunda reta: '))
side_c = float(input('Digite o comprimento da terceira reta: '))

if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
    if side_a == side_b and side_b == side_c:
        print('É um triângulo EQUILÁTERO!')
    elif side_a == side_b or side_b == side_c or side_c == side_a:
        print('É um triângulo ISÓSCELES!')
    elif side_a != side_b and side_b != side_c:
        print('É um triângulo ESCALENO!')
else:
    print('Não é um triângulo!')
