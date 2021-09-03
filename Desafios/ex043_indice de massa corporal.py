# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo: IMC abaixo de 18,5 - Abaixo do peso; Entre 18,5 e 25 - Peso ideal; De 26 a 30 - Sobrepeso; De 31 a 40 - Obesidade; Acima de 40 - Obesidade Mórbida.

p = float(input('Qual o seu peso em quilos? '))
a = float(input('Qual a sua altura em metros? '))
imc = p / a ** 2
if imc < 18.5:
    print('Seu IMC é {}, sua classificação é ABAIXO DO PESO.'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('Seu IMC é {}, sua classificação é PESO IDEAL.'.format(imc))
elif imc >= 26 and imc <= 30:
    print('Seu IMC é {}, sua classificação é SOBREPESO.'.format(imc))
elif imc >= 31 and imc <= 40:
    print('Seu IMC é {}, sua classificação é OBESIDADE.'.format(imc))
else:
    print('Seu IMC é {}, sua classificação é OBESIDADE MÓRBIDA.'.format(imc))
    