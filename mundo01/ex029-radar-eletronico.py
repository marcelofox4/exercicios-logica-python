# Escreva um programa que leia a velocidade do carro.
# Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada Km acima do limite.

from random import randint

car_speed = randint(70, 100)
traffic_ticket = 0

if car_speed > 80:
    traffic_ticket = (car_speed - 80) * 7
    print('Sua velocidade foi de {} e sua multa voi no valor de R$ {:.2f}'.format(car_speed, traffic_ticket))
print('Dirija com Cuidado!')
