# nome = input('Digite seu nome: ')
# print('Prazer em te conhecer {:-^20}!'.format(nome))
# Esquerda{:<}  Direita{:>}   Centro{:^}

n1 = int(input('digite um numero: '))
n2 = int(input('Digite outro numero: '))
s = n1 + n2
sub = n1 - n2
d = n1 / n2
m = n1 * n2
di = n1 // n2
po = n1 ** n2
re = n1 % n2
print('A soma: {}\n a subtração: {}\n divisão: {:.3f}\n multiplicação: {}\n divisão real: {}\n potência: {}\n resto: {}'.format(s,sub,d,m,di,po,re))
