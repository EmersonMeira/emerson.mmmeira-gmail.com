a = int(input('Primeiro bimestre: '))
while a > 10:
    a = int(input('Voce digitou errado. Primeiro bimestre:' ))
b = int(input('Segundo bimestre: '))
while b > 10:
    b = int(input('Voce digitou errado. Segundo bimestre:' ))
c = int(input('Terceiro bimestre: '))
while c > 10:
    c = int(input('Voce digitou errado. Terceiro bimestre:' ))
d = int(input('Quarto bimestre: '))
while d > 10:
    d = int(input('Voce digitou errado. Quarto bimestre: '))
media = (a + b + c + d) / 4
print('media: {}'.format(media))

