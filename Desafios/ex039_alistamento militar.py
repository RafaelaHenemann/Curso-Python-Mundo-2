# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date, datetime
n = int(input('Qual o ano do seu nascimento (com quatro dígitos)? '))
a = date.today().year
c = a - n
if c < 18:
    print('Você tem {} anos, ainda faltam {} anos para você se alistar.'.format(c, 18 - c))
elif c == 18:
    print('Você tem {}, está na hora de se alistar.'.format(c))
else:
    print('Você tem {}, já se passaram {} anos do seu alistamento.'.format(c, c - 18))
