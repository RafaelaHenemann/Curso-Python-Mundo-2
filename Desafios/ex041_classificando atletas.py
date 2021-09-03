# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: Até 9 anos - MIRIM; Até 14 anos - INFANTIL; Até 19 anos - JÚNIOR; Até 25 anos - SÊNIOR; Acima de 25 anos - MASTER.

from datetime import date, datetime
n = int(input('Em que ano o atleta nasceu (quatro dígitos)? '))
a = date.today().year
i = a - n
if i <= 9:
    print('O atleta tem {} anos, portanto está na categoria MIRIM.'.format(i))
elif i > 9 and i <= 14:
    print('O atleta tem {} anos, portanto está na categoria INFANTIL.'.format(i))
elif i > 14 and i <= 19:
    print('O atleta tem {} anos, portanto está na categoria JÚNIOR.'.format(i))
elif i > 19 and i <= 25:
    print('O atleta tem {} anos, portanto está na categoria SÊNIOR.'.format(i))
else:
    print('O atleta tem {} anos, portanto está na categoria MASTER.'.format(i))
    