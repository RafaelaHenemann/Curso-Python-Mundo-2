# Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: EQUILÁTERO - Todos os lados iguais; ISÓSCELES - Dois lados iguais, um diferente; ESCALENO - Todos os lados diferentes.

print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
    if r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
        print('O triângulo formado é do tipo ISÓSCELES.')
    elif r1 == r2 and r2 == r3:
        print('O triângulo formado é do tipo EQUILÁTERO.')
    else:
        print('O triângulo formado é do tipo ESCALENO.')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')
