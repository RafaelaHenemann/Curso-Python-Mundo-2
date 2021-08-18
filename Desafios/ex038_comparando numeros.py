# Escreva um programa que leia dois números inteiros e compare-os. Mostrando na tela uma das seguintes mensagens: O primeiro valor é maior; O segundo valor é maior; Não existe valor maior, os dois são iguais.

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
if n1 > n2:
    print('O primeiro número digitado foi {}, o segundo foi {}. \nO primeiro número é maior!'.format(n1, n2))
elif n2 > n1:
    print('O primeiro número digitado foi {}, o segundo foi {}. \nO segundo número é maior!'.format(n1, n2))
else:
    print('O dois números digitados foram {}. \nOs dois números são iguai!'.format(n1))
  