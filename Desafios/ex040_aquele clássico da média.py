# Crie um programa que leia duas notas de um aluno e calcule a média, mostrando uma mensagem no final, de acordo com a média atingida: Média abaixo de 5.0 - REPROVADO; Média entre 5.0 e 6.9 - RECUPERAÇÃO; Média acima de 7.0 - APROVADO.
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
if m < 5.0:
    print('Sua média foi {:.1f}, infelizmente você foi reprovado!'.format(m))
elif m >= 5.0 and m <= 6.9:
    print('Sua média foi {:.1f}, você está de recuperação.'.format(m))
else:
    print('Sua média foi {:.1f}, parabéns pela aprovação!'.format(m))
    