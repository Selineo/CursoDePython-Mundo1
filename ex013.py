v1 = float(input('valor em dinheiro R$:'))
v2 = int(input('valor da porcentagem a somar:%'))
s1 = (v1 * v2)/100
print('a soma de {}% ao valor original de R${:.3f} e de R${:.3f}'.format(v2, v1, (s1 + v1)))

