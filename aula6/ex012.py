#aumento salario 15%
salario = float(input('Qual seu salario?: '))
aum = (salario * 15)/100
novoSal = salario + aum
print('Seu aumento será de {}R$ e seu novo salario será de {}R$'.format(aum, novoSal))
