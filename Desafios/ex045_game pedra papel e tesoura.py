# Crie um jogo de jokenpô, onde o usuário pode jogar com o computador.

from time import sleep
from random import randint
print('Vamos jogar jokenpô!')
print('Escolha uma opção:\n'
'[1] para PEDRA;\n'
'[2] para PAPEL;\n'
'[3] para TESOURA;')
n = int(input('Qual opção você escolhe? '))
c = randint(1,3)
if n == 1 and c == 1:
    sleep(1) 
    print('Você escolheu PEDRA, o computador também. Empate!')
elif n == 1 and c == 2:
    sleep(1)
    print('Você escolheu PEDRA, o computador escolheu PAPEL. Você perdeu!')
elif n == 1 and c == 3:
    sleep(1)
    print ('Você escolheu PEDRA, o computador escolheu TESOURA. Você ganhou!')
elif n == 2 and c == 1:
    sleep(1)
    print('Você escolheu PAPEL, o computador escolheu PEDRA. Você ganhou!')
elif n == 2 and c == 2:
    sleep(1)
    print('Você escolheu PAPEL, o computador também. Empate!')
elif n == 2 and c == 3:
    sleep(1)
    print('Você escolheu PAPEL, o computador escolheu TESOURA. Você perdeu!')
elif n == 3 and c == 1:
    sleep(1)
    print('Você escolheu TESOURA, o computador escolheu PEDRA. Você perdeu!')
elif n == 3 and c == 2:
    sleep(1)
    print('Você escolheu TESOURA, o computador escolheu PAPEL. Você ganhou!')
else:
    sleep(1)
    print('Você escolheu TESOURA, o computador também. Empate!')
print('Legal! Quer jogar de novo?')
