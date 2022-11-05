# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200 Km e R$ 0,45 para viagens mais longas.

trip_distance = float(input('Digite o Km da viagem: '))
ticket_price = 0

if trip_distance <= 200:
    ticket_price = 0.5 * trip_distance
else:
    ticket_price = 0.45 * trip_distance

print('O valor da passagem é {}.'.format(ticket_price))
