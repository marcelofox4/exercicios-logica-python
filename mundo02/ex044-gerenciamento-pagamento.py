# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

# À vista no Dinheiro: 10% desconto;
# À vista no Cartão: 5% de desconto;
# Em até 2x no Cartão: Preço Normal;
# 3x o mais no Cartão: 20% de juros;

product_price = float(input('Digite o valor a ser pago: '))
discount = 0
print('''[1] À Vista no Dinheiro
[2] À Vista no Cartão
[3] Em até 2x no Cartão
[4] 3x ou mais no Cartão''')

choice_payment = int(input('Digite a opção de pagamento: '))

if choice_payment == 1:
    discount = product_price * (10 / 100)
    print(f'''Valor do Produto: R${product_price}
Valor o Desconto: R${discount}
Total a Pagar: R${(product_price - discount):.2f}''')

elif choice_payment == 2:
    discount = product_price * (5 / 100)
    print(f'''Valor do Produto: R${product_price}
Valor o Desconto: R${discount}
Total a Pagar: R${(product_price - discount):.2f}''')

elif choice_payment == 3:
    print(f'''Valor do Produto: R${product_price}
Valor o Desconto: R${discount}
Total a Pagar: R${(product_price - discount):.2f}
3 parcelas: R${((product_price - discount) / 3):.2f}''')

elif choice_payment == 4:
    installments = int(input('Em quantas parcelas: '))
    discount = product_price * (20 / 100)
    print(f'''Valor do Produto: R${product_price}
Valor dos Juros: R${discount}
Total a Pagar: R${(product_price + discount):.2f}
{installments} parcelas: R${((product_price - discount) / installments):.2f}''')

else:
    print('Essa opção de pagamento não existe!')
