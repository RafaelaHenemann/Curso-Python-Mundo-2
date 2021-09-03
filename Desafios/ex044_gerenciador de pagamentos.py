# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: à vista dinheiro/cheque - 10% de desconto; à vista no cartão - 5% de desconto; em até 2x no cartão - preço normal; 3x ou mais no cartão - 20% de juros.

p = float(input('Qual o valor do produto que você está comprando? R$'))
print('Formas de Pagamento:\n'
'[1] A vista no dinheiro/cheque - 10% de desconto\n'
'[2] A vista no cartão - 5% de desconto\n'
'[3] Em até 2x no cartão de crédito - Preço normal do produto\n'
'[4] Em 3x ou mais no cartão de crédito - 20% de juros')
f = int(input('Qual opção de pagamento acima você gostaria de escolher (indique o número)? '))
if f == 1:
    print('Você escolheu pagar a vista no dinheiro/cheque, seu produto no valor de R${:.2f}, terá 10% de desconto e ficará por R${:.2f}.'.format(p, p - (p * 10 / 100)))
elif f == 2:
    print('Você escolheu pagar a vista no cartão, seu produto no valor de R${:.2f}, terá 5% de desconto e ficará por R${:.2f}.'.format(p, p - (p * 5 / 100)))
elif f == 3:
    print('Você escolheu pagar em 2x no cartão, seu produto no valor de R${:.2f}, manterá seu valor e suas parcelas saírão por R${:.2f} cada.'.format(p, p / 2))
elif f == 4:
    pa = int(input('Em quantas parcelas gostaria de fazer? '))
    print('Você escolheu parcelar o seu produto em {} vezes, haverá um acréscimo de 20% no valor, portanto seu produto que era R${:.2f} passará a custar R${:.2f}, e cada uma das parcelas sairá por R${:.2f}.'.format(pa, p, p + (p * 20 / 100), (p + (p * 20 / 100)) / pa))
else:
    print('Opção inválida, reinicie o processo.')