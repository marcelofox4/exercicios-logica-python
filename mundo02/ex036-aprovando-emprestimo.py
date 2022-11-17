# Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o emprestimo será negado.

house_price = float(input('Digite o preço da casa: '))
buyer_salary = float(input('Digite o salário do comprador: '))
years_pay = int(input('Digite a quantidade de anos para finalizar o pagamento: '))

installment = house_price / (years_pay * 12)

if installment <= buyer_salary * (30 / 100):
        print(f'''Empréstimo concedido!
Valor da Casa: R$ {house_price:.2f}
Valor das parcelas: R$ {installment:.2f}
Tempo do empréstimo: {years_pay}''')
    
else:
    print('Não é possível realizar o empréstimo.')
