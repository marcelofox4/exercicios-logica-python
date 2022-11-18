# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

# Abaixo de 18.5 = Abaixo do Peso;
# Entre 18.5 e 24.9 = Peso Ideal;
# Entre 25 e 29.9 = Excesso de peso;
# 30 até 34.9 = Obesidade I;
# 35 ate 39.9 = Obesidade II;
# Acima ou igual 40 = Obsidade III (Mórbida)

weight = float(input('Digite o seu Peso: '))
height = float(input('Digite a sua Altura: '))
bmi = weight / (height * height)

if bmi < 18.5:
    print('Seu IMC é {:.1f}. Você está abaixo do peso.'.format(bmi))
elif bmi < 24.9:
    print('Seu IMC é {:.1f}. Você está com o peso ideal.'.format(bmi))
elif bmi < 29.9:
    print('Seu IMC é {:.1fvv}. Você está com excesso de peso.'.format(bmi))
elif bmi < 34.9:
    print('Seu IMC é {:.1f}. Você está com obesidade I.'.format(bmi))
elif bmi < 39.9:
    print('Seu IMC é {:.1f}. Você está com obesidade II.'.format(bmi))
else:
    print('Seu IMC é {:.1f}. Você está com obesidade III.'.format(bmi))
