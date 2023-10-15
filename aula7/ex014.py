dias = int(input('Quantos dias o carro foi alugado?: '))
km = float(input('Quantos KM foram percorridos?: '))
total = (dias * 60) + (km * 0.15)
print('O valor total será de: {:.2f}'.format(total))
