# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

# Até 9 anos: MIRIM;
# Até 14 anos: INFANTIL;
# Até 19 anos: JUNIOR;
# Até 20 anos: SÉNIOR;
# Acima: MASTER.

from datetime import date

birth_year = int(input('Digite o ano do seu nascimento: '))
age = date.today().year - birth_year

if age <= 9:
    print('Sua idade é {}\nCategoria: MIRIM.'.format(age))
elif age <= 14:
    print('Sua idade é {}\nCategoria: INFANTIL.'.format(age))
elif age <= 19:
    print('Sua idade é {}\nCategoria: JUNIOR.'.format(age))
elif age <= 20:
    print('Sua idade é {}\nCategoria: SÉNIOR.'.format(age))
else:
    print('Sua idade é {}\nCategoria: MASTER.'.format(age))
