# Altura e largura da parede
w = float(input('Qual a largura da parede?: '))
h = float(input('Qual a altura da parede?: '))
a = w * h
litros = a / 2
print('Area = {}m² e para pintar tudo é necessario {} litros de tinta'.format(a, litros))
