# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:

# Se ele ainda vai se alistar no serviço militar;
# Se é a hora de se alistar;
# Se já passou do tempo de alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

birth_year = int(input('Digite o ano de nascicento: '))
age = date.today().year - birth_year

if age < 18:
    print('Ainda faltam {} anos para o alistamento militar.'.format(18 - age))
elif age > 18:
    print('Já se passaram {} anos para o alistamento militar\nCompareçer na Junta do Serviço Militar'.format(age - 18))
else:
    print('Compareça a junta do Serviço Militar para fazer o alistamento!')
