# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binária, 2 para octal e 3 para hexadecimal.

n = int(input('Digite um número inteiro: '))
b = int(input('Para qual base numérica você gostaria de converter esse número? \nDigite 1 para base binárias \nDigite 2 para base octal \nDigite 3 para base hexadecimal \nOpção escolhida: '))
if b == 1:
    print('O número {} em base binária é igual a {}.'.format(n, bin(n)[2:])) # o código [2:] não mostra os dois primeiro caracteres identificadores da base numérica que está sendo utilizada.
elif b == 2:
    print('O número {} em base octal é igual a {}.'.format(n, oct(n)[2:]))
else:
    print('O número {} em base hexadecimal é igual a {}.'.format(n, hex(n)[2:]))
