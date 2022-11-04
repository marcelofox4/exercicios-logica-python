# Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

temperature_celsius = float(input('Digite a temperatura em gruas Celcius para a conversão: '))
fahrenheit = (temperature_celsius * 1.8) + 32

print('A temperatura em Fahrenheit é {}°'.format(fahrenheit))
