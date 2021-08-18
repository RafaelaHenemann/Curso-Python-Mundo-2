# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

s = float(input('Qual é o seu salário? R$ '))
c = float(input('Qual o valor da casa que gostaria de comprar? R$ '))
a = int(input('Em quantos ANOS você gostaria de pagar? '))
pa = a * 12
pre = c / pa
print('Em {} anos você terá {} parcelas, cada uma no valor de R$ {:.2f}.'.format(a, pa, pre))
if pre > (s * 30/100):
    print('Infelizmente o valor da parcela excede 30% do seu salário. O empréstimo não foi aprovado')
else:
    print('Parabéns, seu empréstimo foi aprovado')
