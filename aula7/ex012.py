#aumento salario 15%
salario = float(input('Qual seu salario?: '))
aum = (salario * 15)/100
novoSal = salario + aum
print('Seu aumento será de {:.2f}R$ e seu novo salario será de {:.2f}R$'.format(aum, novoSal))
